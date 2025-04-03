# Fun-o-Meter

**⚠️ Disclaimer:**  
This is a learning and demo project. It was created for the joy of learning and experimenting with real-time data processing, emotion recognition, and dashboarding.  
There is **no claim to correctness or completeness**, and **no liability** is accepted for any damage that may occur from using this code.

---

## 🎯 Project Idea

This project was born out of the motivation to present a **live Power BI / Fabric dashboard** filled with real-time data during the **data:unplugged** event.

As passionate fans of both **Power BI / Microsoft Fabric** and **gaming**, we initially considered capturing gameplay data via **camera or HDMI capture** and analyzing it using **OCR** – a kind of digital retrofit approach.

However, during a session at the **TDWI Barcamp**, someone pointed out:  
> *“These values are already visible in-game – there's little added value.”*

💡 This shifted our perspective: Instead of focusing on game data, why not analyze **the players themselves**?

Inspired by platforms like **Twitch**, where viewers enjoy watching others play – especially reacting emotionally – we had a new idea:

👉 **Let’s analyze the facial emotions of the players** in real time and integrate this into a live dashboard.

In this way, the player influences the dashboard not just through gameplay, but also through **emotions**!

---

## 🧠 Tech Stack & Tools

Thanks to powerful Python modules and a helpful push from ChatGPT, this idea quickly became a working prototype.

### Used Technologies:

- `Python 3`
- [`DeepFace`](https://github.com/serengil/deepface) for facial emotion analysis
- `OpenCV` for webcam input
- `Azure Event Hub` to stream real-time data
- `Power BI / Microsoft Fabric` for dashboarding

---

## 🚀 Getting Started

> ⚠️ I’m not (yet) a Python expert – but here’s how I got it running:

### 1. Install Python  
You can install Python directly from the Microsoft Store.  
![Microsoft Store Python](imgs/Microsoft%20Store%20Python.png)

---

### 2. Use Visual Studio Code + Python Extension  
I recommend using **Visual Studio Code** with the official **Python extension**.  
![VS Code Python Extension](imgs/VS%20Code%20Python%20Extension.png)

---

### 3. Create a Virtual Environment  
Use separate environments for each Python project. The VS Code extension helps you create one easily:  
![Create Environment](imgs/VS%20Code%20Python%20Create%20Environment.png)  

![Venv Setup](imgs/VS%20Code%20Python%20Venv.png)  

![Interpreter Path](imgs/VS%20Code%20Python%20Interpreter%20Path.png)  

![Install Requirements](imgs/VS%20Code%20Python%20Requirements.png)

---

### 4. Manually Install Missing Modules  
Not all modules were installed from `requirements.txt`, so I activated the `venv` and manually installed the missing ones:

```bash
.venv\Scripts\activate
pip install deepface
pip install azure-eventhub
pip install tf-keras
```

---

### 5. Connect to Azure Event Hub  
To stream the analyzed emotions into **Microsoft Fabric**, you need a connection string from an **Azure Event Hub**.  
You can configure it as a custom endpoint in an eventstream.  
➡️ [Microsoft Learn: Add custom endpoint or app source to Eventstream](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-custom-app?pivots=enhanced-capabilities#event-hub)

---

## 🙌 Acknowledgments

This project was inspired by a mix of:

- A spontaneous idea at a community event
- The creative feedback from the TDWI Barcamp
- The amazing work done by the Python open-source community
- The magic of experimenting with new tech just for fun

---

## 🧪 What’s Next?

This is just the beginning! You’re welcome to:

- Fork, modify, and extend this project
- Connect it with your own dashboards
- Combine it with game mechanics or streaming platforms

Have fun exploring and experimenting!

---

## 📬 Contact

Feel free to reach out on LinkedIn or GitHub if you want to exchange ideas or contribute.

Happy learning! 🚀
