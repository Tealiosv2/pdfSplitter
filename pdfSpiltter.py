import pypdf

def split_pdf_by_range(input_pdf, output_pdf, start_page, end_page):
    with open(input_pdf, 'rb') as file:
        reader = pypdf.PdfReader(file)
        writer = pypdf.PdfWriter()

        # Adjust for zero-based indexing
        for page_number in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_number])

        # Save the specified page range as a new PDF
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

        print(f"Saved pages {start_page} to {end_page} as {output_pdf}")

# Usage
input_pdf = 'input.pdf'
output_pdf = 'output.pdf'

split_pdf_by_range(input_pdf, output_pdf, 1, 10)