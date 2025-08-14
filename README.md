# Task-2
AUTOMATED REPORT GENERATION

## 📄 Automated Sales Report Generator (Python + FPDF)

This Python script creates a *professional PDF sales report* from structured data, including *summary statistics* and a *detailed sales table*.
It’s ideal for *business analytics, **report automation, or **data presentation* projects.

---

### 🚀 Features

* *Dynamic Data Input*: Handles structured sales data (Date, Region, Sales).
* *Statistical Insights*:

  * Average Sales
  * Maximum Sales
  * Minimum Sales
* *Formatted PDF Output*:

  * Custom title, header, and footer.
  * Table with borders for clarity.
* *Cross-Platform Auto Open*:

  * Automatically opens the generated PDF on *Windows, macOS, and Linux*.

---

### 🛠 Technologies Used

* *Python* (Core language)
* *FPDF* (fpdf) – PDF generation library
* *OS & Platform* – Detects the operating system to open files automatically

---

### 📂 How It Works

1. *Data Setup*

   * A predefined list of dictionaries represents daily sales by region.
   * Example:

     python
     {"Date": "2025-06-15", "Region": "North", "Sales": 1500}
     

2. *Statistics Calculation*

   * Extracts sales figures to compute *average, **maximum, and **minimum* values.

3. *PDF Creation*

   * Custom PDF class extends FPDF to include:

     * Title header
     * Page numbers in the footer
   * Adds *summary section* and a *table* with date, region, and sales.

4. *Saving & Opening*

   * Saves the report as sales_report.pdf.
   * Detects the operating system and opens the PDF automatically.

---

### ▶ How to Run

bash
# Install dependencies
pip install fpdf

# Run the script
python Index2.py


---

### 📸 Example Output

The script generates a PDF like this:

```
Sales Report
-----------------------------
Summary of Sales (from 'sales_data.csv')
Average Sales: 1700.00
Maximum Sales: 1900
Minimum Sales: 1500

+------------+---------+-------+
| Date       | Region  | Sales |
+------------+---------+-------+
| 2025-06-15 | North   | 1500  |
| 2025-06-16 | South   | 1800  |
...
``
