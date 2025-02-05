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

def read_file():
    """Prompt the user for a file path and read its content."""
    file_path = input("Enter the path to the log file: ").strip()
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def analyze_log_with_tulu3(log_content):
    """Send the log content to the tulu3 model for analysis."""
    if not log_content:
        print("No log content to analyze.")
        return

    # Construct the prompt
    prompt = f"""
    Analyze the provided kernel call trace to determine the cause of the Out Of Memory (OOM) kill for the flasherav process.

Specifically, focus on:

Memory Allocation Pattern:
Identify the sequence of function calls leading to the memory allocation failure.
Determine the type of memory being allocated (e.g., page cache, kernel stack, user space).
Analyze if there are any signs of excessive memory usage or fragmentation.

System Memory Pressure:
Examine the Mem-Info section to assess the overall memory usage and availability.
Pay attention to metrics like active_anon, inactive_anon, free, slab_reclaimable, and swap.
Look for signs of high memory usage, low free memory, or excessive swap usage.

Process Memory Usage:
Analyze the [ pid ] uid tgid total_vm rss cpu oom_adj oom_score_adj name section to identify processes consuming significant memory.
Look for processes with high rss (Resident Set Size) values.

Potential Causes:
Memory leaks in the flasherav process or other processes.
Excessive memory consumption due to high CPU load or resource-intensive tasks.

Insufficient memory resources on the system.
Misconfiguration of memory parameters (e.g., low swap space).
Additional Considerations:

Time of Occurrence: Determine the time of the OOM kill and correlate it with any recent events (e.g., system load spikes, application launches).
System Load: Analyze system load averages (using top or uptime) around the time of the OOM kill to see if the system was under heavy load.
Other Logs: Examine other system logs (e.g., syslog, dmesg) for any related errors or warnings.
    """

    # Run the tulu3 model with the prompt
    print("Sending log content to tulu3 model for analysis...")
    result = subprocess.run(
        ["ollama", "run", "tulu3"],
        input=prompt.encode(),
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

    # Step 3: Prompt the user for the log file path and analyze it
    log_content = read_file()

    # Step 4: Analyze the log content using the tulu3 model
    if log_content:
        analyze_log_with_tulu3(log_content)
