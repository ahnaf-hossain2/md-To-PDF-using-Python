from fpdf import FPDF
import markdown

# Specify the input Markdown file and output PDF file
input_md_file = 'python_problems.md'  # Replace with your Markdown file name
output_pdf_file = 'python_problems.pdf' # Replace with your desired PDF file name

# Read the Markdown file
with open(input_md_file, 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# Split Markdown into lines for basic processing
lines = markdown_text.split('\n')

# Create a PDF class with custom formatting
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, '50 Basic Python Problems', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 11)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        for line in body:
            if line.strip():  # Skip empty lines
                self.multi_cell(0, 10, line)
        self.ln()

# Initialize PDF
pdf = PDF()
pdf.add_page()

# Process the Markdown lines
current_category = ""
for line in lines:
    if line.startswith('# '):  # Main title
        continue  # Skip adding the main title again since it's in the header
    elif line.startswith('## '):  # Category title
        current_category = line[3:].strip()
        pdf.chapter_title(current_category)
    elif line.strip():  # Problem text
        pdf.chapter_body([line.strip()])

# Save the PDF
pdf.output(output_pdf_file)

print(f"PDF has been generated as '{output_pdf_file}'.")
