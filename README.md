# 🩺 Chat with DOCBOT

An AI-powered medical assistant that analyzes skin conditions from an image and a voice query, providing a diagnosis and remedies in both text and speech.

---

## ✨ Features

-   **Voice Interaction**: Ask questions naturally by recording your voice.
-   **Image Analysis**: Upload an image of a skin condition for the AI to analyze.
-   **AI-Powered Diagnosis**: Leverages a powerful multimodal Large Language Model (Llama via Groq) for analysis.
-   **Accurate Transcription**: Uses OpenAI's Whisper model via the Groq API for fast and precise speech-to-text.
-   **Dual Response**: Get the doctor's response in both written text and a computer-generated voice.
-   **Beautiful & Modern UI**: A responsive and visually appealing interface built with Gradio.

---

## ⚙️ How It Works

The application follows a simple, powerful workflow:

1.  **Input**: The **Gradio** interface captures the user's uploaded image and recorded audio.
2.  **Transcription**: The audio is sent to the **Groq API** and transcribed into text using the **Whisper** model.
3.  **Analysis**: The transcribed text (the user's question) and the encoded image are sent to a multimodal **Llama LLM** via the Groq API.
4.  **Response Generation**: The LLM analyzes the inputs and generates a medical opinion based on the visual and textual data.
5.  **Speech Synthesis**: The text response is converted back into speech using the `pyttsx3` library.
6.  **Output**: All results are displayed back to the user in the Gradio interface.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.9+
-   `pipenv` for managing dependencies. If you don't have it, install it with `pip install pipenv`.
-   A **Groq API Key**. You can get one for free from the [Groq Console](https://console.groq.com/keys).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/VivekChouhan1/Chat_with_DOCBOT.git](https://github.com/VivekChouhan1/Chat_with_DOCBOT.git)
    cd Chat_with_DOCBOT
    ```

2.  **Install dependencies:**
    Use `pipenv` to create a virtual environment and install the required packages from the `Pipfile`.
    ```bash
    pipenv install
    ```

3.  **Activate the environment:**
    ```bash
    pipenv shell
    ```

4.  **Set up your API Key:**
    Create a file named `.env` in the main project directory. Add your Groq API key to this file:
    ```
    GROQ_API_KEY="gsk_YourGroqApiKeyHere"
    ```

### Running the Application

Once the setup is complete, you can start the application with a single command:

```bash
python gradio_app.py
