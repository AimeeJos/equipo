from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    PageTemplate,
    Frame,
    Paragraph,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
from socket import gethostname
from reportlab.lib.units import inch
from django.conf import settings
from bs4 import BeautifulSoup
from reportlab.lib.utils import ImageReader
import os


# Define custom header
def header(canvas, doc, logo):
    canvas.saveState()
    # Add your logo
    logo_path = os.path.join(settings.MEDIA_ROOT, "logos", logo)
    if os.path.exists(logo_path):  # Check if file exists
        logo = ImageReader(logo_path)
        canvas.drawImage(
            logo, inch, 10 * inch, width=100, height=50
        )  # Adjust width and height as needed
    canvas.drawString(inch, 9.6 * inch, "CONSULTATION REPORT")  # Add your logo
    canvas.restoreState()


# Define custom footer
def footer(canvas, doc, ip_address):
    # Define timestamp and IP
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # ip_address = gethostname()  # Replace with actual IP if available
    canvas.saveState()
    footer_text = f"This report is generated on {timestamp} from {ip_address}"
    page_number = canvas.getPageNumber()
    canvas.drawString(inch, 0.75 * inch, footer_text)
    canvas.drawString(7 * inch, 0.75 * inch, f"Page {page_number}")
    canvas.restoreState()


# Define custom PageTemplate with header and footer
class CustomPageTemplate(PageTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logo = None
        self.ip = None

    def afterDrawPage(self, canvas, doc):
        header(canvas, doc, self.logo)
        footer(canvas, doc, self.ip)

    def set_logo_and_ip(self, logo, ip):
        self.logo = logo
        self.ip = ip


def create_pdf_document(data):
    # Create PDF document
    directory = os.path.join(settings.MEDIA_ROOT, "REPORTS")
    print(f"____directory___{directory} exists?: {os.path.exists(directory)}")
    # print(os.path.exists(directory))
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = f"CR_{data.get('PATIENT LAST')}_{data.get('PATIENT FIRST')}_{data.get('PATIENT DOB')}.pdf"
    print(file_name, "=================")
    # file_name = "CR_Doe_Jacob_1990-01-01.pdf"
    pdf_file = os.path.join(directory, file_name)
    pdf = SimpleDocTemplate(
        pdf_file, pagesize=letter, leftMargin=0.5 * inch, topMargin=inch
    )  # Move 0.5 inch from left and 1 inch from top

    return (pdf, file_name, pdf_file)


def generate_pdf(data):

    pdf, file_name, pdf_file = create_pdf_document(data)
    # Create a Frame instance
    frame = Frame(1 * inch, 0.5 * inch, 6 * inch, 9 * inch, id="normal")
    # Add PageTemplate to the document
    custom_template_obj = CustomPageTemplate(id="custom_template", frames=[frame])
    print("======== template")
    custom_template_obj.set_logo_and_ip(
        logo=data.get("LOGO"), ip=data.get("IP ADDRESS")
    )
    pdf.addPageTemplates(custom_template_obj)
    # Convert data dictionary into a list of lists with each key-value pair in a box and bold key
    table_data = []
    for key, value in data.items():
        if key in ["CHIEF COMPLAINT", "CONSULTAION NOTE", "LOGO"]:

            # Parse HTML content using BeautifulSoup
            soup = BeautifulSoup(value, "html.parser")
            # Extract text from parsed HTML
            text = soup.get_text()
            # Check if value has any inline styles (e.g., font-size)
            inline_style = ""
            if "style" in value:
                # Extract inline style from the HTML
                style_start = value.find("style=") + len("style=")
                style_end = value.find('"', style_start + 1)
                inline_style = value[style_start:style_end]
            # Define custom paragraph style based on inline styles
            custom_style = ParagraphStyle(
                f"{key.lower()}_style",
                parent=getSampleStyleSheet()["BodyText"],
                fontSize=10,  # Default font size
                leading=16,  # Default leading
            )
            if inline_style:
                # Parse inline style and extract font size
                for style in inline_style.split(";"):
                    if "font-size" in style:
                        font_size = int(style.split(":")[1].strip(" pt"))
                        # Override default font size in the custom style
                        custom_style.fontSize = font_size
            # Add paragraph with custom style to the table data
            table_data.append(
                [
                    Paragraph(f"<b>{key}:</b>", getSampleStyleSheet()["BodyText"]),
                    Paragraph(text, custom_style),
                ]
            )

        else:
            table_data.append(
                [
                    Paragraph(f"<b>{key}:</b>", getSampleStyleSheet()["BodyText"]),
                    Paragraph(value, getSampleStyleSheet()["BodyText"]),
                ]
            )

    # Define style for the table
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center align content
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("SIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Vertically align content
            ("BOX", (0, 0), (-1, -1), 0.1, colors.black),  # Add border to each cell
            ("INNERGRID", (0, 0), (-1, -1), 0.1, colors.black),  # Add inner grid
        ]
    )

    # Create table object and apply style
    table = Table(table_data)
    table.setStyle(style)

    # Build PDF document
    pdf.build([table])

    print(f"**PDF generated successfully: {pdf_file}")
    return file_name
