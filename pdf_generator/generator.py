# pdf_generator/generator.py
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrinter

def create_pdf(file_path, subject, sender, receiver, date, body):
    """
    Generate a styled PDF letter using the given inputs.
    """
    # Prepare HTML content
    html = f"""
    <html>
    <head>
    <style>
        body {{ font-family: Tahoma; direction: rtl; padding: 30px; }}
        h1 {{ text-align: center; color: #2c3e50; }}
        .header {{ border-bottom: 2px solid #2c3e50; padding-bottom: 10px; margin-bottom: 20px; }}
        .meta {{ margin: 20px 0; font-size: 14px; }}
        .body {{ line-height: 1.8; font-size: 14px; text-align: justify; }}
        .footer {{ margin-top: 40px; text-align: left; font-size: 14px; }}
    </style>
    </head>
    <body>
        <div class="header">شرکت نمونه ایرانیان</div>
        <h1>{subject}</h1>
        <div class="meta">
            <p><b>فرستنده:</b> {sender}</p>
            <p><b>گیرنده:</b> {receiver}</p>
            <p><b>تاریخ:</b> {date}</p>
        </div>
        <div class="body">{body}</div>
        <div class="footer"><p>با احترام،</p><p>{sender}</p></div>
    </body>
    </html>
    """

    # Create QTextDocument and print to PDF
    doc = QTextDocument()
    doc.setHtml(html)

    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setPaperSize(QPrinter.A4)
    printer.setOutputFileName(file_path)
    printer.setFullPage(True)

    doc.print_(printer)
