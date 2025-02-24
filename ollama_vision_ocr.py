import ollama
import base64

def encode_image(image_path):
    """Encodes an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def run_llama3_vision(image_path, prompt):
    """Runs Llama 3.2 Vision with Ollama and an image."""
    try:
        encoded_image = encode_image(image_path)
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [encoded_image]
            }]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

def get_user_input():
    """Gets image path and prompt from the user."""
    image_path = input("Enter the path to the image: ")
    prompt = input("Enter your prompt: ")
    return image_path, prompt

if __name__ == "__main__":
    image_path, user_prompt = get_user_input()
    output = run_llama3_vision(image_path, user_prompt)
    print(output)

    another_query = input("Do you want to run another query with the same image? (yes/no): ").lower()
    if another_query == "yes":
        new_prompt = input("Enter a new prompt: ")
        output2 = run_llama3_vision(image_path, new_prompt)
        print(output2)

    different_image = input("Do you want to run a query with a different image? (yes/no): ").lower()
    if different_image == "yes":
        image_path2, user_prompt3 = get_user_input()
        output3 = run_llama3_vision(image_path2, user_prompt3)
        print(output3)
