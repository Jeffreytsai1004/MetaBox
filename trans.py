import os

# Path to the files to check and convert
directory = 'Scripts/Animation/aTools/animTools'

# Iterate through all files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            # Read the original file, assuming the original encoding is latin-1
            with open(file_path, 'r', encoding='latin-1') as infile:
                content = infile.read()

            # Add content to new UTF-8 encoded file
            with open(file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(content)

            print(f'File {file_path} has been converted to UTF-8 encoding.')
        except Exception as e:
            print(f'Error processing file {file_path}: {e}')