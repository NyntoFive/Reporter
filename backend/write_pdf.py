
from weasyprint import HTML, CSS
def generate_pdf(url, pdf_file):
    """Generate PDF version of the provided URL."""
    print("Generating PDF...")
    css = CSS(string='body{ font-size: 8px; }')
    HTML(url).write_pdf(pdf_file, stylesheets=[css])


if __name__ == '__main__':
    url = 'https://knifekits.com/vcom/index.php'
    pdf_file = 'demo_page.pdf'
    generate_pdf(url, pdf_file)