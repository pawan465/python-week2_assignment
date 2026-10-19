"""Assignment 2: count words, lines, and characters in a text file."""

file_name = input("Enter the name or path of a text file: ").strip()

try:
    # Read the whole file so we can count its words, lines, and characters.
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    lines = text.splitlines()

    print(f"Words: {len(words)}")
    print(f"Lines: {len(lines)}")
    print(f"Characters: {len(text)} (including spaces and line breaks)")

except FileNotFoundError:
    print("File not found. Check the file name and try again.")
except OSError as error:
    print(f"Could not read the file: {error}")
