import io
import csv
import PyPDF2
import re


link_file = io.open("./Exercise_Files/find_the_link.csv")

csv_link = csv.reader(link_file)

index = 0
hidden_link = []

for row in list(csv_link):
    hidden_link.append(row[index])
    index += 1

print(f"hidden link: {''.join(hidden_link)}")

link_file.close()

pdf_file = io.open("./Exercise_Files/Find_the_Phone_Number.pdf", "rb")


pdf_reader = PyPDF2.PdfReader(pdf_file)

for row in pdf_reader.pages:
    match = re.search(r"\d{3}.\d{3}.\d{4}", row.extract_text())
    if match:
        print(match.group())
        break

