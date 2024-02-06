# RPRT Report Generator

This Flask application generates a PDF donation report based on user inputs such as name, amount donated, and causes selected. The generated report includes a personalized thank you message and images related to the selected causes.

## Features

- User-friendly web interface for entering donation details.
- Integration with Cloudinary for fetching images.
- PDF generation with ReportLab library.
- Flask-Bootstrap and Flask-WTF for form styling and validation.

## Product Screenshot
![main-page](https://github.com/mozeezy/rprt/blob/main/screenshots/main-page.png?raw=true)

## Installation

1. **Clone the repository (SSH):**

   ```bash
   git clone git@github.com:mozeezy/rprt.git
   cd rprt
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Setup your Cloudinary environment variables:**
   ```bash
   export CLOUD_NAME=your_cloud_name
   export API_KEY=your_api_key
   export API_SECRET=your_api_secret
   ```
4. **Get the Public ID for the different pages of the PDF:**
   - Within the repository's "assets" folder, you can locate the images utilized by this application. However, you have the flexibility to utilize any templates that suit your preferences.
   - If you opt to use different templates, upload them to your Cloudinary account and obtain the Public ID for each template. The Public ID is crucial for fetching the images from Cloudinary.
   - Ensure that you store the acquired Public IDs as environmental variables.

5. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

1. Visit the web interface at http://127.0.0.1:5000/.
2. Fill out the donation form with the required details.
3. Click the "Generate Report" button to create a PDF report.
4. Download the generated report.


## Configuration
- Adjust the form fields, causes, and styling in the Flask application as needed.
- Customize the thank you message in the **generate_pdf_report** function in **helpers.py** 

## Acknowledgements

- Flask
- Flask-Bootstrap
- Flask-WTF
- ReportLab
- Cloudinary