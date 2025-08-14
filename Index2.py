import csv
from fpdf import FPDF
from fpdf import FPDF
import os
import platform

# Sample data
data = [
    {"Date": "2025-06-15", "Region": "North", "Sales": 1500},
    {"Date": "2025-06-16", "Region": "South", "Sales": 1800},
    {"Date": "2025-06-17", "Region": "East", "Sales": 1700},
    {"Date": "2025-06-18", "Region": "West", "Sales": 1600},
    {"Date": "2025-06-19", "Region": "Central", "Sales": 1900},
]

# Calculate statistics
sales = [row["Sales"] for row in data]
average = sum(sales) / len(sales)
maximum = max(sales)
minimum = min(sales)

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Sales Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(0, 10, "Summary of Sales (from 'sales_data.csv')", ln=True)
pdf.ln(5)
pdf.cell(0, 10, f"Average Sales: {average:.2f}", ln=True)
pdf.cell(0, 10, f"Maximum Sales: {maximum}", ln=True)
pdf.cell(0, 10, f"Minimum Sales: {minimum}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(40, 10, "Date", 1)
pdf.cell(60, 10, "Region", 1)
pdf.cell(40, 10, "Sales", 1)
pdf.ln()

pdf.set_font("Arial", '', 12)
for row in data:
    pdf.cell(40, 10, row["Date"], 1)
    pdf.cell(60, 10, row["Region"], 1)
    pdf.cell(40, 10, str(row["Sales"]), 1)
    pdf.ln()

# Save PDF
pdf_file = "sales_report.pdf"
pdf.output(pdf_file)
print(f"✅ PDF saved as '{pdf_file}'.")

# Automatically open PDF
if platform.system() == "Windows":
    os.startfile(pdf_file)
elif platform.system() == "Darwin":  # macOS
    os.system(f"open {pdf_file}")
else:  # Linux
    os.system(f"xdg-open {pdf_file}")