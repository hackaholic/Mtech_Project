import base64
import requests
import re
import os

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

def save_diagram(name, code):
    # Mermaid.ink expects base64 encoded string
    # Using the standard format for mermaid.ink
    # Simple base64 encoding of the utf-8 string
    base64_string = base64.b64encode(code.encode('utf-8')).decode('ascii')
    
    url = f"https://mermaid.ink/img/{base64_string}"
    print(f"Downloading {name} from {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(f"{name}.png", 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved {name}.png")
        else:
            print(f"Failed to download {name}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

def main():
    if not check_internet():
        print("No internet connection detected. Cannot use mermaid.ink service.")
        return

    file_path = "uml_diagrams.md"
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Regex to find mermaid blocks
    # Looking for ```mermaid ... ```
    pattern = r"```mermaid\n(.*?)```"
    matches = re.findall(pattern, content, re.DOTALL)

    filenames = ["efficientnet_workflow", "resnet_workflow"]
    
    if len(matches) != len(filenames):
        print(f"Warning: Found {len(matches)} diagrams but expected {len(filenames)}.")
    
    for i, code in enumerate(matches):
        if i < len(filenames):
            save_diagram(filenames[i], code.strip())
        else:
            save_diagram(f"diagram_{i+1}", code.strip())

if __name__ == "__main__":
    main()
