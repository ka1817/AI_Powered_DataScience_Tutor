## AI Powered DataScience Tutor 

AI Tutor - Streamlit & FastAPI 🚀

This project is an AI-powered tutoring app that uses FastAPI as the backend and Streamlit as the frontend. The application is containerized using Docker and managed via Docker Compose. It also requires a Groq API key for AI responses.

Project Structure
The project is structured as follows:

Backend: Contains FastAPI code for handling AI queries.
Frontend: Contains Streamlit code for the user interface.
Docker Compose: Manages both services in containers.
Environment Variables: Stores API keys and configurations.
Prerequisites
Before running the project, ensure you have:

Docker installed on your system.
Groq API Key for AI functionality.
Git (optional, for cloning the repository).
Setup & Installation
Cloning the Repository
Download the project from GitHub using git clone, then navigate into the project directory.

Setting Up Environment Variables
Create a .env file in the project directory and add your Groq API Key.

Running the Application
Use docker-compose up --build to start both the backend and frontend containers.

Usage
Once the application is running:

Frontend (Streamlit): Accessible via http://localhost:8501
Backend (FastAPI): Accessible via http://localhost:8000/docs
API Endpoints (FastAPI)
The backend provides the following API endpoints:

POST /ask - Sends a user question to the AI tutor.
GET /health - Checks if the backend is running.
Docker Setup (Manual)
If running containers manually:

Build and run the backend container.
Build and run the frontend container.
Ensure environment variables are correctly passed.
Troubleshooting
Frontend Fails to Connect to Backend
Ensure the backend is running and logs show no errors.
Check the FASTAPI_URL in app.py and update it accordingly.
If running without Docker, change the backend URL to http://127.0.0.1:8000/ask.
API Key Issues
Check if .env file is correctly set.
Manually export the key if needed.
Contributing
To contribute:

Fork the repository.
Create a new branch for your feature.
Commit your changes.
Push to GitHub and create a Pull Request.

Author
Developed by Pranav Reddy.