# MedScanAI

## 📌 Overview
MedScanAI is an AI-powered medical diagnosis tool designed to assist in detecting abnormalities in medical scans, recognizing medicines, and providing mental health assessments. It integrates deep learning models for accurate predictions and offers a user-friendly interface for seamless interaction.
---
## 🚀 Features
- ✅ **Medical Scan Analysis** – Detect abnormalities in X-rays using CNN models.
- ✅ **Medicine Recognition** – Identify medicines using AI.
- ✅ **Doctor & Pharmacy Locator** – Find nearby doctors and pharmacies using Google Maps API.
- ✅ **Mental Health Assessment** – AI-based mental health evaluation tools.
- ✅ **AI Chatbot Support** – Get health-related guidance and answers through an intelligent AI chatbot.
- ✅ **User Login & Authentication** – Secure login system using Node.js and MongoDB.
- ✅ **User-Friendly Interface** – Intuitive UI for easy access to medical predictions.

---
## 🖥️ Screenshots

### 🔹 Dashboard

https://github.com/user-attachments/assets/26fcbda8-3453-473a-b891-87df811b2215

### 🔹 Medical Scan Analysis
![Dashboard](https://github.com/user-attachments/assets/aa0d7cab-fc62-4f56-83ff-b40cfb9638c4)
![Medical Scan Analysis](https://github.com/user-attachments/assets/29b850e7-0659-4003-951f-8eba8644c9c6)

### 🔹 Medicine Recognition
![Medicine Recognition](https://github.com/user-attachments/assets/6afc6d39-ff96-42fc-9214-0542ac8ac0a9)

### 🔹 Doctor & Pharmacy Locator
![Doctor & Pharmacy Locator](https://github.com/user-attachments/assets/f550a814-fd9d-4558-af69-4558f5b40db7)

### 🔹 Mental Health Assessment
![Mental Health Assessment](https://github.com/user-attachments/assets/31f78854-5272-4123-9d41-1c48611f9ae0)

### 🔹 AI Chatbot
![AI Chatbot](https://github.com/user-attachments/assets/example-chatbot-screenshot)

### 🔹 Conclusion
![User-Friendly Interface](https://github.com/user-attachments/assets/29273a0a-2140-4919-8d3c-1a187146f94e)

---

## 📂 Tech Stack
- **Machine Learning & Deep Learning** – TensorFlow, PyTorch, OpenCV
- **Frontend** – HTML, CSS, JavaScript
- **Backend** – Flask / Django (for AI models), Node.js (for authentication)
- **Database** – MongoDB (for user login system), Firebase / PostgreSQL (optional for other features)
- **APIs** – Google Maps API
- **Chatbot** – OpenAI GPT / Dialogflow (custom integration)

---

## 🔐 Authentication Module
- Built using **Node.js**, **Express**, and **MongoDB**
- Supports **JWT-based login/signup**
- User credentials are stored securely in **MongoDB**
- Middleware to protect medical prediction routes for authenticated users

---

## 🧠 AI Chatbot
- Integrated an AI chatbot using **OpenAI GPT API**
- Responds to common medical queries and guides users through the platform
- Available on every page via a chat icon popup

---

## Backend – Auth System (Node.js)
# Navigate to auth directory
cd auth

# Install Node.js dependencies
npm install

# Start the server
node index.js



## 🔧 Installation & Setup

### Backend – AI Models (Python)
```sh
# Clone the repository
git clone https://github.com/ayush07mishra/MedScanAI.git
cd MedScanAI

# Install Python dependencies
pip install -r requirements.txt

# Run Flask App
python app.py
