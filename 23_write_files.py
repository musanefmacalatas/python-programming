# Example 1: Writing to a file
with open ("new products.txt", "w") as file:
    # Open (or create) "new products.txt" in write mode ("w").
    # This will overwrite the file if it already exists.
          file.write("\nSHORTS, 250")
    # Write a new line with "SHORTS, 250" to the file.
print("\n")

# Example 2: Appending to a file
with open ("new products.txt", "a") as file:
    # Open "new products.txt" in append mode ("a").
    # This adds new content to the end of the file without overwriting.
          file.write("\nT-SHIRTS, 350")
    # Append "T-SHIRTS, 350" as a new line in the file.
print("\n")

# Example 3: Reading the file

with open ("new products.txt", "r") as file:
    # Open "new products.txt" in read mode ("r").
          print(file.read())

    # Read the entire file and display all its contents.
print("\n")

# demo (APPEND WITHOUT seek(0))
with open("demo.txt", "a+") as file:
    # Open "demo.txt" in append+read mode ("a+").
    # If the file does not exist, it will be created.

    file.write("\nITEM A, 100")
    # Append a new line containing "ITEM A, 100" at the end of the file.

    print("Pointer after write:", file.tell())
    # file.tell() shows the current file pointer position (in bytes).
    # After writing, the pointer stays at the end of the file.

    print("Read content:", file.read())
    # Since the pointer is already at the end, file.read() returns nothing (empty string).

print("\n")

# demo (APPEND WITH seek(0))
with open("demo.txt", "a+") as file:
    # Open the same file again in append+read mode.

    file.write("\nITEM B, 200")
    # Append another line containing "ITEM B, 200".

    print("Pointer after write:", file.tell())
    # Show the pointer position after writing (still at the end of the file).

    file.seek(0)
    # Move the pointer back to the beginning of the file.

    print("Read content:", file.read())
    # Now read() will return the entire content of the file,
    # including both old and newly appended lines.

print("\n")

# demo (just read to confirm FILE content)
with open("demo.txt", "r") as file:
    # Open the file in read-only mode.

    print("Final file content:\n", file.read())
    # Display the final content of the file,
    # confirming all previous write and append operations.

