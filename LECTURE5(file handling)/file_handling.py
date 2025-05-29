# Appending to a file
with open("tinah.txt", "a") as file:
    file.write("This is an appended line.\n")

# Reading the file again to see the changes
with open("tinah.txt", "r") as file:
    content = file.read()
    print(content)
