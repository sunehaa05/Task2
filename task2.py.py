import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Read data from CSV
data = pd.read_csv("covid_data1.csv")

# Step 2: Analyze data (calculate totals)
total_cases = data["Cases"].sum()
total_deaths = data["Deaths"].sum()
total_recovered = data["Recovered"].sum()

# Step 3: Generate PDF Report
pdf_file = "covid_report.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 20)
c.drawString(200, height - 50, "COVID-19 Report")

# Subtitle
c.setFont("Helvetica", 12)
c.drawString(50, height - 100, "Summary of COVID-19 Data:")

# Write totals
c.drawString(50, height - 130, f"Total Cases: {total_cases}")
c.drawString(50, height - 150, f"Total Deaths: {total_deaths}")
c.drawString(50, height - 170, f"Total Recovered: {total_recovered}")

# Add table header
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 220, "Country")
c.drawString(150, height - 220, "Cases")
c.drawString(250, height - 220, "Deaths")
c.drawString(350, height - 220, "Recovered")

# Add table rows
c.setFont("Helvetica", 12)
y = height - 240
for index, row in data.iterrows():
    c.drawString(50, y, str(row["Country"]))
    c.drawString(150, y, str(row["Cases"]))
    c.drawString(250, y, str(row["Deaths"]))
    c.drawString(350, y, str(row["Recovered"]))
    y -= 20

# Save PDF
c.save()
print("PDF Report Generated Successfully: covid_report.pdf")
