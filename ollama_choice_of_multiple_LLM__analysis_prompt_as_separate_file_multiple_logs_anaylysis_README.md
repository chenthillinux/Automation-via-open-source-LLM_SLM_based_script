# Ollama Log Analyzer

This Python script automates the process of analyzing log files using Large Language Models (LLMs) through Ollama. It handles Ollama installation, model downloading, reading log and prompt files, and sending the content to the selected LLM for analysis.

## Features

* **Automated Ollama Installation:** Installs Ollama if it's not already present on the system.
* **LLM Selection:** Allows users to choose from a list of available LLMs (tulu3, phi4, deepseek-r1:8b).
* **Model Pulling:** Automatically downloads the selected LLM from Ollama.
* **Prompt File Input:** Reads prompts from a user-specified file.
* **Multiple Log File Input:** Reads content from multiple log files specified by the user.
* **Log Analysis:** Sends the combined prompt and log content to the selected LLM for analysis.
* **Displays Model Output:** Prints the LLM's response to the console.

## Prerequisites

* **Python 3:** Ensure Python 3 is installed.
* **Internet Connection:** Required for downloading Ollama and LLMs.

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
    python3 ollama_choice_of_multiple_LLM__analysis_prompt_as_separate_file_multiple_logs_anaylysis.py
    ```

2.  **LLM Selection:**
    * The script will display a list of available LLMs.
    * Enter the number corresponding to your desired LLM (1, 2, or 3) which provide choice of LLM like tulu3 , phi4 and deepseek .

3.  **Prompt File Path:**
    * Enter the full path to your prompt file. This file should contain the instructions or questions you want the LLM to answer about the log files.

4.  **Log File Paths:**
    * Enter the full path to each log file you want to analyze, one at a time.
    * Type `done` and press Enter when you have finished entering log file paths.

5.  **Analysis and Output:**
    * The script will send the combined prompt and log content to the selected LLM.
    * The LLM's response will be displayed in the console.

## Script Explanation

* **`install_ollama()`:** Checks if Ollama is installed and installs it if necessary.
* **`pull_model(model_name)`:** Downloads the specified LLM from Ollama.
* **`read_prompt_file()`:** Reads the prompt from the specified file.
* **`read_log_files()`:** Reads the content of multiple log files as specified by the user.
* **`analyze_log(log_content, prompt_content, model_name)`:** Combines the prompt and log content, sends it to the LLM, and prints the response.
* **`if __name__ == "__main__":`:** The main execution block of the script, handling user input, model selection, and log analysis.


