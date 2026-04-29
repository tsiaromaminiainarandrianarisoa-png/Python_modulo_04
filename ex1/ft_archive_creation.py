import sys

def display_contents()-> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name)
    except Exception as error:
        print(f"Error opening file '{file_name}': {error}")
    else:
        print("---")
        content = f.read()
        print(content)
        print(f"\n---\nFile '{file_name}' closed.")
        print("\nTransform data:\n---\n")
        f.close()
        contents = content.rsplit('\n')
        if len(contents) == 1:
            new_contents = contents[0] + "#\n"
        else:
            new_contents = contents[0]
            for line in contents[1:]:
                new_contents = "#\n".join([new_contents, line])
        print(f"{new_contents}\n---")
        new_file = input("Enter new file name (or empty): ")
        if not new_file:
            print("Not saving data.")
        else:
            try:
                nf = open(new_file, "w")
                nf.write(new_contents)
                nf.close()
                print(f"Saving data to '{new_file}'")
                print(f"Data saved in file '{new_file}'.\n")
            except Exception as error:
                print(f"Error opening file '{file_name}': {error}")

if __name__ == "__main__":
     display_contents()


