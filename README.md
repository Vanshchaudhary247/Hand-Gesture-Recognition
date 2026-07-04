# Hand Gesture Recognition using MediaPipe and OpenCV

## 📌 Project Overview

This project is a real-time Hand Gesture Recognition System developed using Python, OpenCV, and MediaPipe. It detects hand landmarks through a webcam, recognizes simple hand gestures, and maps them to system actions.

## ✨ Features

- Real-time webcam hand tracking
- Detects 21 hand landmarks using MediaPipe
- Recognizes multiple hand gestures:
  - 👍 Thumbs Up
  - ✋ Open Palm
  - ✊ Fist
- Maps gestures to system actions:
  - Thumbs Up → Play/Pause
  - Open Palm → Volume Up
  - Fist → Volume Down
- Displays detected gesture on the screen

---

## 🛠 Technologies Used

- Python 3.11
- OpenCV
- MediaPipe
- PyAutoGUI

---

## 📂 Project Structure

```
Hand-Gesture-Recognition/
│── app.py
│── gesture.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Vanshchaudhary247/Hand-Gesture-Recognition.git
```

Go to the project directory:

```bash
cd Hand-Gesture-Recognition
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

Press **Q** to close the application.

---

## 🎮 Gesture Mapping

| Gesture | Action |
|----------|--------|
| 👍 Thumbs Up | Play / Pause |
| ✋ Open Palm | Increase Volume |
| ✊ Fist | Decrease Volume |

---

## 📷 Output

- Detects hand landmarks in real time.
- Displays the recognized gesture on the webcam feed.
- Performs the corresponding system action.

---

## 📋 Requirements

- Python 3.11+
- Webcam
- Windows Operating System

---

## 📚 Libraries

- OpenCV
- MediaPipe
- PyAutoGUI

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Improvements

- Add more hand gestures.
- Control mouse cursor using hand tracking.
- Gesture-based presentation controller.
- Gesture-controlled media player.
- Improve gesture accuracy using machine learning.

---

