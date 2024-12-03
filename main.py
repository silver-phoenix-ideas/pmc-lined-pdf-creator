# Imports
import pandas
from fpdf import FPDF

# Configurations
rgb_grey = (120, 120, 120)
rgb_white = (255, 255, 255)

# Document
pdf = FPDF("portrait", "mm", "A4")
pdf.set_auto_page_break(False, 0)
pdf.set_text_color(*rgb_grey)

# Pages
data = pandas.read_csv("data/topics.csv")

for i, row in data.iterrows():
    for j in range(row["Pages"]):
        pdf.add_page()

        # Header
        txt_header = row["Topic"] if not j else ""
        pdf.set_font("Times", "B", 24)
        pdf.cell(0, 12, txt_header, 0, 1, "L")

        draw_color = rgb_grey if not j else rgb_white
        pdf.set_draw_color(*draw_color)
        pdf.line(10, 21, 200, 21)

        # Blank Space
        pdf.ln(265)

        # Footer
        txt_footer = row["Topic"] + " (cont.)" if j else row["Topic"]
        pdf.set_font("Times", "I", 8)
        pdf.cell(0, 10, txt_footer, 0, 1, "R")

# Output File
pdf.output("files/python-study-notebook.pdf")
