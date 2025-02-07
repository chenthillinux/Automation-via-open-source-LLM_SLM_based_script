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

def pull_model(model_name):
    """Pull the specified model using Ollama."""
    print(f"Pulling {model_name} model...")
    subprocess.run(["ollama", "pull", model_name], check=True)
    print(f"{model_name} model pulled successfully.")

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

def analyze_log(log_content, prompt_content, model_name):
    """Send the log content to the specified model for analysis using the provided prompt."""
    if not log_content:
        print("No log content to analyze.")
        return

    # Construct the full prompt by combining prompt and log content
    full_prompt = f"{prompt_content}\n\nLog Content:\n{log_content}"

    # Run the model with the full prompt
    print(f"Sending log content to {model_name} model for analysis...")
    result = subprocess.run(
        ["ollama", "run", model_name],
        input=full_prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Print the model's response
    if result.returncode == 0:
        print(f"{model_name} Model Analysis:")
        print(result.stdout.decode())
    else:
        print(f"Error running the {model_name} model:")
        print(result.stderr.decode())

if __name__ == "__main__":
    # Step 1: Install Ollama (if not already installed)
    install_ollama()

    # Step 2: Allow user to select the LLM
    print("Select the LLM to use:")
    print("1. tulu3")
    print("2. phi4")
    print("3. deepseek")
    model_choice = input("Enter your choice (1-3): ")

    # Map user choice to model name
    model_names = {
        "1": "tulu3",
        "2": "phi4",
        "3": "deepseek-r1:8b"
    }
    selected_model = model_names.get(model_choice)

    if selected_model:
        # Step 2: Pull the selected model
        pull_model(selected_model)

        # Step 3: Prompt the user for the prompt file path and read its content
        prompt_content = read_prompt_file()

        # Step 4: Prompt the user for the log file path and read its content
        log_content = read_log_file()

        # Step 5: Analyze the log content using the selected model
        if log_content and prompt_content:
            analyze_log(log_content, prompt_content, selected_model)
    else:
        print("Invalid model choice.")