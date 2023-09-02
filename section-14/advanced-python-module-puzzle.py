# import shutil
import os
import io
import re

# shutil.unpack_archive("./unzip_me_for_instructions.zip")

# print(os.listdir("./extracted_content"))
# print(io.open("./extracted_content/Instructions.txt").read())

for folder, sub_folders, files in os.walk("./extracted_content"):
    for file in files:
        file_content = io.open(f"{folder}/{file}").read()
        telephone_number = re.search(r"\d{3}-\d{3}-\d{4}", file_content)
        if telephone_number:
            print(f"The telephone number is at: {folder}/{file}")
            print(telephone_number.group())
            break

