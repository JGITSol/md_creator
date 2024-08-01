import os
import pyperclip

DEFAULT_HEADER = """   $$$$$\  $$$$$$\        $$$$$$\ $$$$$$$$\        $$$$$$\            $$\             $$\     $$\                               
   \__$$ |$$  __$$\       \_$$  _|\__$$  __|      $$  __$$\           $$ |            $$ |    \__|                              
      $$ |$$ /  \__|        $$ |     $$ |         $$ /  \__| $$$$$$\  $$ |$$\   $$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$$\ 
      $$ |$$ |$$$$\         $$ |     $$ |         \$$$$$$\  $$  __$$\ $$ |$$ |  $$ |\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$  _____|
$$\   $$ |$$ |\_$$ |        $$ |     $$ |          \____$$\ $$ /  $$ |$$ |$$ |  $$ |  $$ |    $$ |$$ /  $$ |$$ |  $$ |\$$$$$$\  
$$ |  $$ |$$ |  $$ |        $$ |     $$ |         $$\   $$ |$$ |  $$ |$$ |$$ |  $$ |  $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
\$$$$$$  |\$$$$$$  |      $$$$$$\    $$ |         \$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
 \______/  \______/       \______|   \__|          \______/  \______/ \__| \______/    \____/ \__| \______/ \__|  \__|\_______/ 
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                              $$\ $$\                                                                           
                                              $$ |$$ |                                                                          
 $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$$ |$$ |$$\   $$\                                                                 
$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$ |$$ |$$ |  $$ |                                                                
$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ |$$ |  $$ |                                                                
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |                                                                
$$$$$$$  |$$ |      \$$$$$$  |\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$ |                                                                
$$  ____/ \__|       \______/  \______/  \_______|\__| \____$$ |                                                                
$$ |                                                  $$\   $$ |                                                                
$$ |                                                  \$$$$$$  |                                                                
\__|                                                   \______/                                                                 
                                                             $$\                                                                
                                                             $$ |                                                               
 $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\  $$$$$$$\ $$$$$$\    $$$$$$$\ $$\                                              
$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$  __$$\\_$$  _|  $$  _____|\__|                                             
$$ /  $$ |$$ |  \__|$$$$$$$$ |\$$$$$$\  $$$$$$$$ |$$ |  $$ | $$ |    \$$$$$$\                                                   
$$ |  $$ |$$ |      $$   ____| \____$$\ $$   ____|$$ |  $$ | $$ |$$\  \____$$\ $$\                                              
$$$$$$$  |$$ |      \$$$$$$$\ $$$$$$$  |\$$$$$$$\ $$ |  $$ | \$$$$  |$$$$$$$  |\__|                                             
$$  ____/ \__|       \_______|\_______/  \_______|\__|  \__|  \____/ \_______/                                                  
$$ |                                                                                                                            
$$ |                                                                                                                            
\__|                           """

DEFAULT_FOOTER = """        _                                                          _                     _             _     _        __               _     
   __ _| |_      ____ _ _   _ ___    ___ _   _ _ __ _ __ ___ _ __ | |_    ___ ___  _ __ | |_ __ _  ___| |_  (_)_ __  / _| ___     __ _| |_ _ 
  / _` | \ \ /\ / / _` | | | / __|  / __| | | | '__| '__/ _ \ '_ \| __|  / __/ _ \| '_ \| __/ _` |/ __| __| | | '_ \| |_ / _ \   / _` | __(_)
 | (_| | |\ V  V / (_| | |_| \__ \ | (__| |_| | |  | | |  __/ | | | |_  | (_| (_) | | | | || (_| | (__| |_  | | | | |  _| (_) | | (_| | |_ _ 
  \__,_|_| \_/\_/ \__,_|\__, |___/  \___|\__,_|_|  |_|  \___|_| |_|\__|  \___\___/|_| |_|\__\__,_|\___|\__| |_|_| |_|_|  \___/   \__,_|\__(_)
    _       _ _         |___/        _ _   _           _      _                                                                              
   (_) __ _(_) |_ ___  ___ | |  __ _(_) |_| |__  _   _| |__  (_) ___                                                                         
   | |/ _` | | __/ __|/ _ \| | / _` | | __| '_ \| | | | '_ \ | |/ _ \                                                                        
   | | (_| | | |_\__ \ (_) | || (_| | | |_| | | | |_| | |_) || | (_) |                                                                       
  _/ |\__, |_|\__|___/\___/|_(_)__, |_|\__|_| |_|\__,_|_.__(_)_|\___/ """
DEFAULT_DESCRIPTION = """The given Python script generates a customized README.md file for a project. It prompts the user to input the project name and description, and then constructs the README content by combining a predefined header, an ASCII art representation of the project name, the user-provided description, and a footer.

The key functionalities of the script include:

Reading optional header and footer content from external files (if available).
Collecting user input for the project name and description.
Creating an ASCII art representation of the project name.
Constructing the final README.md content by combining all the elements.
The generated README.md file serves as documentation for the project, providing essential information for users and contributors.
WRITTEN AND TESTED MANUALLY (WORKING w/o bugs) ON WIN 64, PYTHON 3.11.3"""

def read_file(filename, default_content):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using default content.")
        return default_content

def get_long_input(prompt):
    print(f"{prompt} (Press Enter, then Ctrl+V to paste, then Enter again to finish)")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)

def generate_ascii_art(text):
    # This is a simple ASCII art generator. For more complex designs,
    # you might want to use a library like pyfiglet
    result = ""
    for line in text.split('\n'):
        result += f"# {line}\n"
    return result

def main():
    # Read header and footer
    header = read_file("_header.txt", DEFAULT_HEADER)
    footer = read_file("_footer.txt", DEFAULT_FOOTER)
    description = read_file("_description.txt", DEFAULT_DESCRIPTION)
    
    # Get project name
    project_name = input("Enter project name: ")

    # Get short project description
    short_description = input("Enter a one-line project description: ")

    # Read long description from file
    long_description = read_file("description.txt", description)

    # Generate README content
    readme_content = f"""
{header}

{generate_ascii_art(project_name)}

{short_description}

{long_description}

{footer}
"""

    # Write to README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    print("README.md has been generated successfully!")

if __name__ == "__main__":
    main()