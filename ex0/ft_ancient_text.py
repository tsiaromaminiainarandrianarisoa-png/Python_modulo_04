import sys

def display_contents()-> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    try:
        print(f"Accessing file '{file_name}'")
        fd = open(file_name)
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    else:
        print("---\n")
        print(fd.read())
        print(f"\n---\nFile '{file_name}' closed.")
        fd.close()

if __name__ == "__main__":
    display_contents()

