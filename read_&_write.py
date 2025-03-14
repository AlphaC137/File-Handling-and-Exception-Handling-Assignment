def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
          
        modified_content = content.upper()
        
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File '{input_filename}' has been read, modified, and written to '{output_filename}'.")
    
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def open_file_with_error_handling():
    filename = input("Please enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File content of '{filename}':")
        print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Welcome to the File Read & Write and Error Handling Program!")
    
    choice = input("Do you want to read, modify, and write a file? (yes/no): ").lower()
    if choice == 'yes':
        input_file = input("Enter the filename to read: ")
        output_file = input("Enter the filename to write modified content: ")
        read_and_modify_file(input_file, output_file)
    
    choice = input("Do you want to read a file with error handling? (yes/no): ").lower()
    if choice == 'yes':
        open_file_with_error_handling()

if __name__ == "__main__":
    main()
