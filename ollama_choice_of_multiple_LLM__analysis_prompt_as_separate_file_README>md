# Ollama Log Analyzer (Single Log File)

This Python script utilizes Ollama to analyze a single log file using a Large Language Model (LLM). It automates the installation of Ollama (if not already present), downloads the selected LLM, reads a prompt from a file, reads the log file content, and sends both to the LLM for analysis.

## Features

* **Automated Ollama Installation:** Installs Ollama if it is not found on the system.
* **LLM Selection:** Allows users to choose from a list of predefined LLMs (tulu3, phi4, deepseek-r1:8b).
* **Model Downloading:** Automatically downloads the selected LLM using Ollama.
* **Prompt File Input:** Reads the analysis prompt from a user-specified text file.
* **Single Log File Input:** Reads the content of a single log file specified by the user.
* **Log Analysis:** Combines the prompt and log content and sends it to the selected LLM for analysis.
* **Displays Model Output:** Prints the LLM's response to the console.

## Prerequisites

* **Python 3:** Ensure Python 3 is installed on your system.
* **Internet Connection:** Required for downloading Ollama and the LLM.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```
    (Replace `[repository URL]` and `[repository directory]` with your actual repository information.)

## Usage

1.  **Run the Script:**
    ```bash
    python3 ollama_choice_of_multiple_LLM__analysis_prompt_as_separate_file.py
    ```

2.  **Select LLM:**
    * The script will display a list of available LLMs.
    * Enter the number corresponding to your desired LLM (1, 2, or 3)  which provide choice of LLM like tulu3 , phi4 and deepseek .

3.  **Prompt File Path:**
    * Enter the full path to the prompt file. This file should contain the instructions or questions you want the LLM to answer about the log file.

4.  **Log File Path:**
    * Enter the full path to the log file you want to analyze.

5.  **Analysis and Output:**
    * The script will combine the prompt and log content and send it to the selected LLM.
    * The LLM's response will be printed to the console.

## Script Explanation

* **`install_ollama()`:** Checks if Ollama is installed and installs it if necessary.
* **`pull_model(model_name)`:** Downloads the specified LLM using Ollama.
* **`read_prompt_file()`:** Reads the prompt from the specified file.
* **`read_log_file()`:** Reads the content of the specified log file.
* **`analyze_log(log_content, prompt_content, model_name)`:** Combines the prompt and log content, sends it to the selected LLM, and prints the response.
* **`if __name__ == "__main__":`:** The main execution block of the script, handling user input, model selection, and log analysis.

## Example
