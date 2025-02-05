# Kernel Call Trace Analysis with Tulu3

This Python script analyzes kernel call traces to identify the cause of Out Of Memory (OOM) kills. 

Features:

* Installs Ollama if not already present.
* Pulls the Tulu3 8B model using Ollama.
* Prompts the user for the path to a kernel log file.
* Sends the log content to the Tulu3 model for analysis.
* Removes `<think>` sections from the model's output.
* Prints the Tulu3 model's analysis of the OOM kill.

Usage:

1. Install Python and required libraries:
   - Ensure you have Python installed.
   - Install the `subprocess` module (usually included with Python by default).

2. Run the script:
   - Execute the script from your terminal: `python ollama_deepseek_log_analysis.py`
   - The script will:
      - Install Ollama if necessary.
      - Pull the Tulu3 8B model.
      - Prompt you to enter the path to the kernel log file.
      - Send the log content to the Tulu3 model for analysis.
      - Print the model's analysis to the console.

Requirements:

*   Python 3
*   Ollama installed and configured
*   Tulu3 8B model pulled (using Ollama)

Note:

*   This script requires an active internet connection to download Ollama and the Tulu3 model.
*   The effectiveness of the analysis depends on the quality of the Tulu3 model's response and the complexity of the OOM issue.
*   Consider adjusting the model and prompt for specific use cases or refining the analysis based on the model's output.

**Disclaimer:**

This script is provided for informational and educational purposes only. The author is not responsible for any consequences arising from the use of this script. 
