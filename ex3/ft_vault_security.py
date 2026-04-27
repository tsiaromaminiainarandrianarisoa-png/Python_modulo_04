def secure_archive(file_name: str, action: str = '', content: str = '') -> tuple:
	operation = False
	try :
		if action == "" or action == "r":
			with open(file_name) as f:
				content = f.read()
		elif action == "w":
			with open(file_name, "w") as f:
				f.write(content)
				content = "Content successfully written to file"
	except OSError as error:
		content = str(error)
		operation = False
	else:
		operation = True
	return (operation, content)

if __name__ == "__main__":
	print("=== Cyber Archives Security ===")
	print("\nUsing 'secure_archive' to read from a nonexistent file:")
	print(secure_archive("/not/existing/file", "r", "Pakachukabra"))
	print("\nUsing 'secure_archive' to read from an inaccessible file:")
	print(secure_archive("/etc/shadow"))
	print("\nUsing 'secure_archive' to read from a regular file:")
	result = secure_archive("../ex0/ft_ancient_text.py", "r")
	print(result)
	print("\nUsing 'secure_archive' to write previous content to a new file:")
	print(secure_archive("new_file.txt", "w", result[1]))
