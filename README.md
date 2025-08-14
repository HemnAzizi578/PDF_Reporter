
**PDF_Reporter** is a Python-based desktop application built with PyQt5 that allows users to generate professional PDF letters and reports. Users can input details such as subject, sender, receiver, date, and body content, and the application will generate a PDF document based on a predefined template.

## Features

- **User-friendly GUI**: Input fields for subject, sender, receiver, date, and body content.
- **PDF Generation**: Converts input data into a professionally formatted PDF document.
- **Template Customization**: Developers can customize the PDF template to match company branding and formatting requirements.

## Installation

To run the application, ensure you have Python 3.8 or higher installed. Then, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/HemnAzizi578/PDF_Reporter.git
   cd PDF_Reporter

2. Install the required dependencies:

pip install -r requirements.txt


3. Run the application:

python main.py



Usage

1. Launch the application.


2. Fill in the fields:

Subject: Enter the subject of the letter.

Sender: Enter the sender's name.

Receiver: Enter the receiver's name.

Date: Enter the date.

Body: Enter the main content of the letter.



3. Click on the "Generate PDF" button.


4. Choose the location to save the generated PDF file.



Template Customization

The PDF template is defined in the pdf_generator/generator.py file. To customize the appearance of the generated PDFs:

1. Open the pdf_generator/generator.py file.


2. Locate the HTML template string within the file.


3. Modify the HTML and CSS to match your desired layout, fonts, colors, and branding.



Note: Ensure that placeholder variables like {subject}, {sender}, {receiver}, {date}, and {body} remain intact, as they are dynamically replaced with user input.

Project Structure

PDF_Reporter/
│
├── main.py                  # Entry point of the application
├── ui/
│   └── main_window.py       # PyQt5 UI components
├── pdf_generator/
│   └── generator.py         # PDF generation logic and template
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
