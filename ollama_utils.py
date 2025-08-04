import subprocess

def query_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma3:1b", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout:
            return result.stdout.strip()
        else:
            print("No output received from Ollama.")
            return "Sorry, I couldn't get a response."
    except subprocess.CalledProcessError as e:
        print("Ollama command failed:", e)
        print("STDERR:", e.stderr)
        return "Error: Ollama command failed."
    except Exception as e:
        print("Unexpected error:", e)
        return "Error: Something went wrong."

