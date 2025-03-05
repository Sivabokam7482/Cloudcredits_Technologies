import os

def open_file(filename,inital_content):
    # Open a file and read its contents.
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        print("File not found. Creating a new file.")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(inital_content)
        return inital_content
    
    
def save_file(filename, content):
    # Save the content to a file.
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print("File saved successfully.")

def text_editor():
    # A simple command-line text editor.
    filename = input("Enter the filename: ")
    inital_content=input("Enter the content:")
    content = open_file(filename,inital_content)
    
    while True:
        print("\nCurrent Content:")
        print("-" * 40)
        print(content)
        print("-" * 40)
        
        print("\nOptions: [E]dit, [S]ave, [Q]uit")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'e':
            new_content = input("Enter new content: ")
            content = new_content
        elif choice == 's':
            save_file(filename, content)
        elif choice == 'q':
            print("Closing editor.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    text_editor()
