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

## Backend – Auth System (Node.js)
# Navigate to auth directory
cd auth

## Install Node.js dependencies
npm install

## Start the server
node index.js

## 🔧 Installation & Setup

### Backend – AI Models (Python)
```sh
# Clone the repository
git clone https://github.com/ayush07mishra/MedScanAI.git
cd MedScanAI

# Install Python dependencies
pip install -r requirements.txt

#LIVE LINK-> https://medscanai-pksi.onrender.com/




# Run Flask App
python app.py
