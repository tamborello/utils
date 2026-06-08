# Make a bunch of copies of a file


import shutil
import os
from pathlib import Path

# Configuration
source_file = r"C:\Users\ftamborello\OneDrive - Procentrix, Inc\Enterprise Deconfliction Search Tool\PDFs\Frankenstein.pdf"  # source file path
output_dir = r"C:\Users\ftamborello\OneDrive - Procentrix, Inc\Enterprise Deconfliction Search Tool\PDFs\Lots of Frankensteins"  # Update this with desired output directory
num_copies = 5000

# Create output directory if it doesn't exist
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Get the source file name and extension
source_filename = os.path.basename(source_file)
name, ext = os.path.splitext(source_filename)

# Create copies
for i in range(1, num_copies + 1):
    # Generate output file name (e.g., file_1.txt, file_2.txt, etc.)
    output_filename = f"{name}_{i}{ext}"
    output_path = os.path.join(output_dir, output_filename)
    
    # Copy the file
    shutil.copy2(source_file, output_path)
    
    # Print progress every 500 copies
    if i % 500 == 0:
        print(f"Created {i} copies...")

print(f"Successfully created {num_copies} copies of {source_filename}")
