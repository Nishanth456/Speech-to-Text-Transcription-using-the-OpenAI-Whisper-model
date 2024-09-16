# Speech-to-Text Transcription Using the OpenAI Whisper Model

This project provides a speech-to-text transcription tool using the OpenAI Whisper model. It leverages various libraries, including `transformers`, `torch`, `gradio`, `langchain`, `ibm_watson_machine_learning`, and `huggingface-hub`, alongside FFmpeg for audio processing.

## Prerequisites

### 1. Setup Python Virtual Environment

1. **Install `virtualenv` and create a virtual environment:**

    ```bash
    pip install virtualenv
    virtualenv my_env
    my_env\Scripts\activate  # For Windows
    ```

2. **Install required Python libraries:**

    ```bash
    pip install transformers==4.35.2 torch gradio==4.17.0 langchain==0.0.343 ibm_watson_machine_learning==1.0.335 huggingface-hub==0.19.4
    pip install git+https://github.com/openai/whisper.git
    ```

### 2. Download and Install FFmpeg

1. **Download the Correct FFmpeg Version:**

    - Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
    - Choose Windows and select a third-party build (e.g., Gyan.dev).
    - Download the Release Essentials zip file.

2. **Extract and Locate the Bin Folder:**

    - Extract the zip file to a directory, e.g., `C:\ffmpeg\`.
    - Locate the `bin` folder containing `ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe`.

3. **Add FFmpeg to the System Path:**

    - Open `System Properties` > `Advanced System Settings` > `Environment Variables`.
    - Under System variables, find `Path`, and click `Edit`.
    - Click `New` and add the path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
    - Click `OK` to close all windows.

4. **Verify Installation:**

    Open a new command prompt and run:

    ```bash
    ffmpeg -version
    ```

### 3. Configure FFmpeg for the Virtual Environment

1. **Activate Virtual Environment:**

    ```bash
    my_env\Scripts\activate  # For Windows
    ```

2. **Ensure FFmpeg is Accessible:**

    - **Temporary PATH Update:**

      ```bash
      set PATH=%PATH%;C:\ffmpeg\bin
      ```

      Verify with:

      ```bash
      ffmpeg -version
      ```

    - **Permanent PATH Update:**

      - Open `my_env\Scripts\activate.bat`.
      - Add the following line towards the end:

        ```bash
        set PATH=%PATH%;C:\ffmpeg\bin
        ```

      - Restart VSCode and re-activate the virtual environment.

### 4. Upgrade Libraries

Ensure you have the latest versions of `gradio` and `pydantic`:

```bash
pip install --upgrade gradio pydantic
