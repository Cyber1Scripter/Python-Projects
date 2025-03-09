import subprocess

def get_target_url():
    url = input("Enter the target URL: ")
    return url

def get_wordlist_path():
    wordlist_path = input("Enter the path to the directory names list: ")
    return wordlist_path

def run_gobuster(target_url, wordlist_path):
    command = f"gobuster dir -u {target_url} -w {wordlist_path}"
    print(f"Running Gobuster with command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main():
    target_url = get_target_url()
    wordlist_path = get_wordlist_path()
    run_gobuster(target_url, wordlist_path)

if __name__ == "__main__":
    main()
