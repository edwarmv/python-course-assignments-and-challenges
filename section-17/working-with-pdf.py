import PyPDF2
import io

f = io.open("Working_Business_Proposal.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(f)
print(f"number of pdf pages: {len(pdf_reader.pages)}")
page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print(f"page one text:\n{page_one_text}")
f.close()
f = io.open("Working_Business_Proposal.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)
pdf_output = io.open("some_brandnew_doc.pdf", "wb")
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()
f = io.open("Working_Business_Proposal.pdf", "rb")
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())
print(pdf_text[1])
