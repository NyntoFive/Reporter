from weasyprint import HTML, CSS

def generate_pdf(url, pdf_file):
    """Generate PDF file from the provided URL"""
    print("Generating page...")
    css = CSS(string='body{ font-size:8px;}')
    HTML(url).write_pdf(pdf_file, stylesheets=[css])

if __name__ == '__main__':
    url = "http://text.npr.org"
    pdf_file = 'demo_page.pdf'
    generate_pdf(url, pdf_file)