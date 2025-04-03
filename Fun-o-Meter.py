import cv2
import time
import json
from deepface import DeepFace
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# Azure Event Hub Connection String
EVENTHUB_CONNECTION_STR = "Endpoint=sb://eventstream-xxxxxxxx.servicebus.windows.net/;SharedAccessKeyName=key_xxxxxxxx;SharedAccessKey=xxxxxxxx;EntityPath=es_xxxxxxx"
producer = EventHubProducerClient.from_connection_string(conn_str=EVENTHUB_CONNECTION_STR)

# Start camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera could not be opened.")
    exit()

last_time = time.time()
print("Starting emotion analysis... (Press 'q' to quit)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()
    if current_time - last_time >= 1:
        last_time = current_time

        try:
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

            if isinstance(results, list):
                # Sort by X-position (so player 1 is on the left, player 2 on the right)
                sorted_results = sorted(results, key=lambda face: face["region"]["x"])

                output = {
                    "timestamp": datetime.now().isoformat(),
                    "players": []
                }

                for i, face in enumerate(sorted_results):
                    emotions_clean = {k: float(v) for k, v in face["emotion"].items()}
                    player_data = {
                        "id": i + 1,
                        "dominant_emotion": face["dominant_emotion"],
                        "emotions": emotions_clean,
                        "position_x": face["region"]["x"]
                    }
                    output["players"].append(player_data)

                # Send JSON to Event Hub
                event_data = EventData(json.dumps(output))
                with producer:
                    producer.send_batch([event_data])

                print("JSON sent to Event Hub.")

            else:
                print("Only one face detected – skipping.")

        except Exception as e:
            print("Error during analysis:", e)

    cv2.imshow('Webcam Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
