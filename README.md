# MedConnect AI

**Team:** Oana Ilie, Carmen Rațiu, Sabina Radu, Darius Borza  
**Project built at:** RebelDot AI Hackathon 2024 

MedConnect is an AI-powered assistant designed to break language barriers in healthcare by enabling real-time multilingual communication between patients and medical professionals. The application integrates speech recognition, text and image translation, and document processing, offering a seamless communication experience in clinical contexts.

## Features

### 1. Real-time Multilingual Conversations
- Speech-to-Text (STT): Transcribes voice input from users.
- Text Translation: Translates between languages instantly using Google Cloud APIs.
- Text-to-Speech (TTS): Reads translated messages aloud in the target language.

### 2. Image & Document Scanning
- OCR & Translation: Extracts text from medical documents or handwritten notes using OpenCV + Tesseract and translates it.
- Support for scanned images and printed forms.

### 3. Technology Stack
- Frontend: React.js
- Backend: Python
- AI Services: Google Cloud (Translation, TTS, STT)
- Image Processing: OpenCV, Tesseract

## Future Improvements
- Offline Voice Recorder using Raspberry Pi for remote clinics
- Integration with Med-PaLM 2 for medical reasoning
- Use of CNN models to enhance image text extraction
- Database creation and search by CNP (Romanian Personal Numeric Code)

## Demo
A functional prototype was demonstrated at the hackathon. Key flows include:
- Real-time speech translation in a simulated doctor-patient dialogue
- Image scan and translation from printed Romanian medical forms

## Recommended Folder Structure
medconnect-ai/
├── frontend/ # React app
├── backend/ # Python services
├── models/ # Optional: CNN, Med-PaLM2 integration
├── docs/ # Sample scanned images, test forms
├── README.md


## Acknowledgments

Thanks to RebelDot for organizing the AI Hackathon and offering the opportunity to build impactful healthcare tools.

