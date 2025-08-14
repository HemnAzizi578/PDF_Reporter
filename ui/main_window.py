# ui/main_window.py
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton,
    QFileDialog, QMessageBox
)
from pdf_generator.generator import create_pdf
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Reporter")
        self.setGeometry(200, 200, 600, 600)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Subject input
        layout.addWidget(QLabel("Subject:"))
        self.subject_input = QLineEdit()
        layout.addWidget(self.subject_input)

        # Sender input
        layout.addWidget(QLabel("Sender:"))
        self.sender_input = QLineEdit()
        layout.addWidget(self.sender_input)

        # Receiver input
        layout.addWidget(QLabel("Receiver:"))
        self.receiver_input = QLineEdit()
        layout.addWidget(self.receiver_input)

        # Date input
        layout.addWidget(QLabel("Date:"))
        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("e.g., 1404/05/23")
        layout.addWidget(self.date_input)

        # Body input
        layout.addWidget(QLabel("Letter Body:"))
        self.body_input = QTextEdit()
        layout.addWidget(self.body_input)

        # Generate PDF button
        self.generate_btn = QPushButton("Generate PDF")
        layout.addWidget(self.generate_btn)

        # Connect button to handler
        self.generate_btn.clicked.connect(self.handle_generate_pdf)

    # Function to handle PDF generation
    def handle_generate_pdf(self):
        # Collect form data
        subject = self.subject_input.text()
        sender = self.sender_input.text()
        receiver = self.receiver_input.text()
        date = self.date_input.text() or datetime.now().strftime("%Y/%m/%d")
        body = self.body_input.toPlainText()

        # Check if all required fields are filled
        if not subject or not sender or not receiver or not body:
            QMessageBox.warning(self, "Error", "All fields must be filled.")
            return

        # Ask user where to save the PDF
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Letter", "", "PDF Files (*.pdf)")
        if not file_path:
            return

        # Generate the PDF
        create_pdf(file_path, subject, sender, receiver, date, body)
        QMessageBox.information(self, "Success", "PDF generated successfully!")
 