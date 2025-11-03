def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_text_file("dude.txt")