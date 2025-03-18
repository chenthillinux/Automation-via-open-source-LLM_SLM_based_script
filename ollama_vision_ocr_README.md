# Llama 3.2 Vision with Ollama

This Python script utilizes the Llama 3.2 Vision model, accessible through Ollama, to analyze images and provide textual responses based on user-provided prompts.

## Overview

The script allows users to:

* Encode images into base64 format.
* Send images and prompts to the Llama 3.2 Vision model via Ollama.
* Receive and display the model's textual responses.
* Run multiple queries using the same image or switch to a different image.

## Prerequisites

Before running the script, ensure you have the following installed:

* **Ollama:** Download and install Ollama from [ollama.com](https://ollama.com/).
* **Llama 3.2 Vision Model:** Pull the `llama3.2-vision` model using Ollama:
    ```bash
    ollama pull llama3.2-vision
    ```
* **Python 3:** Ensure Python 3 is installed on your system.
* **Ollama Python Library:** Install the `ollama` Python library:
    ```bash
    pip install ollama
    ```

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```
    (Replace `[repository URL]` and `[repository directory]` with the actual repository URL and directory.)

2.  **Run the Script:**
    ```bash
    python ollama_vision_ocr.py

    ```

3.  **Provide Image Path and Prompt:**
    * The script will prompt you to enter the file path of the image you want to analyze.
    * Next, enter your prompt or question related to the image.

4.  **View the Response:**
    * The model's response will be displayed in the console.

5.  **Continue with More Queries:**
    * The script will ask if you want to run another query using the same image. If you choose "yes", you'll be prompted to enter a new prompt.
    * You'll also be asked if you want to analyze a different image. If you choose "yes", you'll need to provide a new image path and prompt.

## Code Breakdown

* **`encode_image(image_path)`:**
    * This function reads an image file in binary mode and encodes it into a base64 string.
    * Base64 encoding is necessary for sending image data through the Ollama API.
* **`run_llama3_vision(image_path, prompt)`:**
    * This function orchestrates the interaction with the Llama 3.2 Vision model.
    * It encodes the image, constructs the message payload for Ollama, and sends the request.
    * It then extracts and returns the model's response.
* **`get_user_input()`:**
    * This function prompts the user to enter the image path and the prompt through the command line.
    * It returns the provided inputs.
* **`if __name__ == "__main__":`:**
    * This is the main entry point of the script.
    * It calls `get_user_input()` to get the image path and prompt.
    * It calls `run_llama3_vision()` to get the model's response and prints it.
    * It handles the logic to repeat the query with the same image, or change to a different image.

## Notes

* Ensure Ollama is running in the background before executing the script.
* The image file must be accessible from the script's location.
* Error handling is included, so error messages will be displayed if something goes wrong.
* This is a simple command line tool, and additional UI could be added.
