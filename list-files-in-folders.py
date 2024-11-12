import os

def get_folder_names():
    return input("Enter folder names separated by spaces: ").split()

def list_files(folder):
    try:
        files = os.listdir(folder)
        print(f"Files in '{folder}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Folder '{folder}' does not exist.")
    except PermissionError:
        print(f"No access to '{folder}'.")

def main():
    folders = get_folder_names()
    for folder in folders:
        list_files(folder)

if __name__ == "__main__":
    main()
