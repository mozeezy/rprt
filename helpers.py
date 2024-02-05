import textwrap
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os
from cloudinary.utils import cloudinary_url


def generate_pdf_report(name, amount_donated, causes, front_page, thank_you_page, final_page, output_filename):

    pdf_canvas = canvas.Canvas(output_filename, pagesize=letter)
    page_width, page_height = letter
    pdf_canvas.setFont("Helvetica", 12)

    pdf_canvas.drawImage(ImageReader(front_page), 0, 0, width=page_width, height=page_height)

    pdf_canvas.showPage()

    formatted_causes = format_causes_list(causes)
    thank_you_text = f"We extend our heartfelt gratitude to you for your generous donation of ${amount_donated:.2f} towards our effort(s) of {formatted_causes}. Your support plays a crucial role in helping us achieve our mission and make a positive impact in the lives of those we serve. Your contribution is not just a financial gift; it is a powerful statement of your commitment to making a difference. With donors like you, we are able to move closer to our shared vision of making the world a better place for everyone around the world. Your generosity inspires us and motivates us to continue our work with passion and dedication. We are privileged to have you as a valued member of our community, and we look forward to keeping you updated on the progress and success stories made possible by your support. Once again, thank you for making a difference. Together, we are creating positive change and building a brighter future."
    thank_you_text_wrapped = textwrap.wrap(thank_you_text, width=75)
    pdf_canvas.drawImage(ImageReader(thank_you_page), 0, 0, width=page_width, height=page_height)
    pdf_canvas.drawString(100, 550, f"Dear {name.title()},")

    y = 520
    for words in thank_you_text_wrapped:
        pdf_canvas.drawString(100, y, words)
        y -= 20

    pdf_canvas.showPage()

    for cause in causes:
        CAUSE_PUBLIC_ID = os.environ.get("CAUSE") + cause.lower()
        cause_image = cloudinary_url(CAUSE_PUBLIC_ID, format="png")[0]
        pdf_canvas.drawImage(ImageReader(cause_image), 0, 0, width=page_width, height=page_height)
        pdf_canvas.showPage()

    pdf_canvas.drawImage(ImageReader(final_page), 0, 0, width=page_width, height=page_height)

    pdf_canvas.save()


def format_causes_list(causes):
    if len(causes) == 0:
        return ""
    elif len(causes) == 1:
        return causes[0]
    elif len(causes) == 2:
        return causes[0] + " and " + causes[1]
    else:
        return ', '.join(causes[:-1]) + ', and ' + causes[-1]
