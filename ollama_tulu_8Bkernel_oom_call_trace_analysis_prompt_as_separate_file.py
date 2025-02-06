import subprocess
import os

def install_ollama():
    """Install Ollama if not already installed."""
    try:
        subprocess.run(["ollama", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Ollama is already installed.")
    except FileNotFoundError:
        print("Ollama not found. Installing Ollama...")
        subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh", "-o", "install_ollama.sh"], check=True)
        subprocess.run(["chmod", "+x", "install_ollama.sh"], check=True)
        subprocess.run(["./install_ollama.sh"], check=True)
        os.remove("install_ollama.sh")
        print("Ollama installed successfully.")

def pull_tulu3_model():
    """Pull the Tulu3 8B model using Ollama."""
    print("Pulling Tulu3 8B model...")
    subprocess.run(["ollama", "pull", "tulu3"], check=True)
    print("Tulu3 8B model pulled successfully.")

def read_prompt_file():
    """Prompt the user for the prompt file path and read its content."""
    prompt_file_path = input("Enter the path to the prompt file: ").strip()
    try:
        with open(prompt_file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Prompt file '{prompt_file_path}' not found.")
        return None

def read_log_file():
    """Prompt the user for the log file path and read its content."""
    log_file_path = input("Enter the path to the log file: ").strip()
    try:
        with open(log_file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
        return None

def analyze_log_with_tulu3(log_content, prompt_content):
    """Send the log content to the tulu3 model for analysis using the provided prompt."""
    if not log_content:
        print("No log content to analyze.")
        return

    # Run the tulu3 model with the prompt
    print("Sending log content to tulu3 model for analysis...")
    result = subprocess.run(
        ["ollama", "run", "tulu3"],
        input=prompt_content.encode(), 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Print the model's response
    if result.returncode == 0:
        print("Tulu3 Model Analysis:")
        print(result.stdout.decode())
    else:
        print("Error running the Tulu3 model:")
        print(result.stderr.decode())

if __name__ == "__main__":
    # Step 1: Install Ollama (if not already installed)
    install_ollama()

    # Step 2: Pull the tulu3 8B model
    pull_tulu3_model()

    # Step 3: Prompt the user for the prompt file path and read its content
    prompt_content = read_prompt_file()

    # Step 4: Prompt the user for the log file path and read its content
    log_content = read_log_file()

    # Step 5: Analyze the log content using the tulu3 model
    if log_content and prompt_content:
        analyze_log_with_tulu3(log_content, prompt_content)