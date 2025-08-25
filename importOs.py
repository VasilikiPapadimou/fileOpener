import os
import sys

def main():
    base_dir = sys.argv[1]       # directory where files should be created
    file_name = sys.argv[2]      # file name without extension
    file_type = sys.argv[3].lower()  # file extension (txt, md, py, etc.)

    # Create base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: {base_dir}")
    #Create the files in the folder
    file_path = os.path.join(base_dir,f"{file_name}.{file_type}").replace("\\", "/")
    #print(file_path)
    #open the file for reading
    with open(file_path, "r") as f:
        print("filepath ->", file_path)
        #f.write(f"This is {file_name}.{file_type} created in {base_dir}\n")
if __name__ == "__main__":
    main()
