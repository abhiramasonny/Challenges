import os

def generate_readme(directory="."):
    readme_title = os.path.basename(os.path.abspath(directory))
    files_and_dirs = os.listdir(directory)
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f)) and f != "README.md"]
    subdirectories = [d for d in files_and_dirs if os.path.isdir(os.path.join(directory, d))]

    with open("README.md", "w") as readme:
        readme.write(f"# {readme_title}\n\n")
        descriptions = []
        for filename in files:
            description = input(f"Enter description for {filename}: ")
            descriptions.append(description)
            readme.write(f"- [{filename}]({filename}): {description}\n")
        
        if files and subdirectories:
            readme.write("\n---\n\n")
        
        for subdirectory in subdirectories:
            generate_readme(os.path.join(directory, subdirectory))
            sub_readme_title = os.path.basename(os.path.abspath(subdirectory))
            readme.write(f"## {sub_readme_title}\n\n")
            readme.write(f"See [{sub_readme_title}/README.md]({sub_readme_title}/README.md) for details.\n\n")

            with open("{subdirectory}/README.md")as current:
                current.write(i for i in descriptions)
                

if __name__ == "__main__":
    generate_readme()
