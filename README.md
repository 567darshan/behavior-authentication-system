
 🚀 Behavior-Based Passwordless Authentication System

 🔐 AI + Cybersecurity Project | Typing Pattern Authentication (Keystroke Dynamics)

This project demonstrates a **passwordless login system** based on **typing behavior** instead of traditional passwords.
Every person has a **unique typing rhythm**, and this project captures that pattern to verify identity.

The system compares:

* The user’s **registered typing pattern**
* The **new typing pattern during login**

If both patterns match within a threshold → **Access Granted**
Else → **Access Denied**

---

## 🌟 Features

### 🔹 **1. Passwordless Login**

No need for passwords — authentication is based on *how* a user types a fixed phrase.

### 🔹 **2. Keystroke Dynamics**

Captures and analyzes:

* Time between key presses
* Typing rhythm
* Typing consistency

### 🔹 **3. FastAPI Backend**

Handles registration, verification, and pattern comparison.

### 🔹 **4. Simple Frontend UI**

A clean web interface built using HTML, CSS, and JavaScript.

### 🔹 **5. Real-Time Authentication**

Compares live typing data against the saved user template.

---

## 🏗️ Project Structure

```
behavior_auth_project/
│
├── backend/
│   ├── main.py               # FastAPI backend
│   └── requirements.txt      # Python dependencies
│
└── frontend/
    └── index.html            # Web UI
```

---

## 🛠️ Technologies Used

### **Frontend**

* HTML
* CSS
* JavaScript

### **Backend**

* Python
* FastAPI
* Uvicorn
* NumPy

---

## ⚙️ How It Works

### **1️⃣ Registration Phase**

* User enters a username
* User types a fixed phrase: `mysecurephrase`
* Typing intervals (time gaps between key presses) are recorded
* Backend stores this pattern as the **user template**

### **2️⃣ Login Verification**

* User types the same phrase again
* New typing pattern is captured
* System compares new pattern vs saved template
* If difference < threshold → user is considered *genuine*

---

## 📦 Installation & Setup

### **Backend Setup**

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Runs at:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### **Frontend Setup**

Simply open:

```
frontend/index.html
```

in your browser.

No extra setup is required.

---

## 🧪 API Endpoints

### **POST /register**

Registers a new typing template.

**Payload:**

```json
{
  "username": "darshan",
  "phrase": "mysecurephrase",
  "intervals": [120, 80, 95, ...]
}
```

---

### **POST /verify**

Verifies if the new typing matches the saved pattern.

**Returns:**

* `genuine_user: true/false`
* `distance`
* `threshold`
* Message: “Access Granted / Denied”

---

 📘 Real-World Applications

This authentication method can be used in:

* Banking fraud detection
* Online exam proctoring
* Secure company logins
* Continuous user verification
* Passwordless authentication systems
* Cybersecurity risk analysis

---

⚠️ Limitations

* Typing behavior changes with mood, stress, or keyboard
* Short phrases give lower accuracy
* Works best on physical keyboards, not mobile typing
* Should be used as an additional security layer, not standalone

---

🚀 Future Scope

* Use machine learning (SVM/KNN) for more accurate classification
* Add mouse movement and touch pressure analysis
* Support mobile typing behavior
* Add multi-factor authentication
* Store templates securely in a database
* Real-time continuous authentication

---

👤 Author
Darshan
Behavior-Based Authentication Prototype – Cybersecurity + AI Project

