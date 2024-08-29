# Define the file name and the content
file_name = "output.txt"
content = """1. Phone 
2. Tablet 
3. RGB Coffee Mug 
4. Keyboard 
5. PC """

# Open the file in write mode and write the content to it
with open(file_name, "w") as file:
    file.write(content)

print(f"Content has been written to {file_name}")

