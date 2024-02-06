from flask import Flask, render_template, request, send_file
import cloudinary
from cloudinary.utils import cloudinary_url
from helpers import generate_pdf_report
import os
from flask_bootstrap import Bootstrap
from forms import ReportForm

app = Flask(__name__)
app.app_context().push()
app.secret_key = "a-random-string"
Bootstrap(app)

cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("API_KEY"),
    api_secret=os.environ.get("API_SECRET")
)

FRONT_PAGE_PUBLIC_ID = os.environ.get("FRONT_PAGE")
THANK_YOU_PAGE_PUBLIC_ID = os.environ.get("THANK_YOU")
FINAL_PAGE_PUBLIC_ID = os.environ.get("FINAL")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReportForm()
    if form.validate_on_submit():
        name = request.form['name']
        amount_donated = float(request.form['amount_donated'])
        causes = request.form.getlist("causes")

        output_filename = f"{name.replace(' ', '_').lower()}_donation_report.pdf"
        front_page = cloudinary_url(FRONT_PAGE_PUBLIC_ID, format="png")[0]
        thank_you_page = cloudinary_url(THANK_YOU_PAGE_PUBLIC_ID, format="png")[0]
        final_page = cloudinary_url(FINAL_PAGE_PUBLIC_ID, format="png")[0]
        generate_pdf_report(name, amount_donated, causes, front_page, thank_you_page, final_page, output_filename)

        return send_file(output_filename, as_attachment=True)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
