# Create and write to the file
try:
    # Open the file in write mode
    with open("my_file.txt", "w") as file:
        # Write three lines of text
        file.write("I can't belive I am learning python this easily.\n")
        file.write("I have spent 1, 2, 3, 4, over 5 weeks even though I wasn't consistent, I am trying to catch up.\n")
        file.write("I believe this will help me in my cyber security journey.\n")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("File creation and writing completed.\n")

# Read and display the file contents
try:
    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read and display the contents
        print("File Contents:")
        print(file.read())
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("\nFile reading and display completed.\n")

# Append 
try:
    # Open the file in append + mode just to check it out
    with open("my_file.txt", "a+") as file:

        # Append three additional lines of text
        file.write("what can I say...\n")
        file.write("Hoping I advance as I am given a good foundation.\n")
        file.write("Thanks to PLP!!!!!!..\n")

        # Move the file pointer to the beginning of the file
        file.seek(0)
        
        # Read and print the file contents
        print("File Contents after appending:")
        print(file.read())
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("File appending completed.\n")