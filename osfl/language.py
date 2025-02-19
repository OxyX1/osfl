# language.py

import requests
from urllib.parse import urlparse

def import_osfl_module_from_github(repo_url):
    """
    Imports an osfl module from the given GitHub repository.
    This function searches for an `osfl.py` file on either the 'main' or 'master' branch.
    
    Parameters:
        repo_url (str): The GitHub repository URL (e.g., 
                        "https://github.com/username/repository")
    
    Returns:
        module (dict): A dictionary representing the module's global namespace.
    
    Raises:
        ValueError: If the provided URL is not a valid GitHub repository URL.
        FileNotFoundError: If the osfl.py file is not found in the repository.
    """
    parsed = urlparse(repo_url)
    if parsed.netloc != "github.com":
        raise ValueError("Provided URL is not a GitHub repository URL.")
    
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub repository URL. Expected format: https://github.com/username/repository")
    
    owner, repo = path_parts[0], path_parts[1]
    branches = ["main", "master"]
    
    for branch in branches:
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/osfl.py"
        print(f"Checking for osfl.py at {raw_url}...")
        response = requests.get(raw_url)
        if response.status_code == 200:
            print(f"Found osfl.py in branch '{branch}'.")
            code = response.text
            module = {}
            exec(code, module)
            return module
        else:
            print(f"osfl.py not found at {raw_url} (status code: {response.status_code}).")
    
    raise FileNotFoundError("osfl.py not found in the provided repository on either 'main' or 'master' branch.")

if __name__ == "__main__":
    repo_url = input("Enter GitHub repository URL: ").strip()
    try:
        module = import_osfl_module_from_github(repo_url)
        print("osfl.py module imported successfully.")

        # Example: if the imported module defines a function named 'run', we can call it.
        if "run" in module:
            print("Running module's 'run' function...")
            module["run"]()
        else:
            print("The imported module does not contain a 'run' function.")
    except Exception as e:
        print("Error:", e)
