# Imports
import pandas
from fpdf import FPDF
import modules.color_palette as rgb
import modules.pdf_helper as pdf_helper

# Sizes
base = 10
step = int(base * 1)
header_font = int(base * 2.5)
header_height = int(header_font / 2.5)
footer_font = int(base * 1)
footer_height = int(footer_font / 2)

# Document
paper = pdf_helper.get_paper("A4")
paper["margin_bottom"] = 10

area = pdf_helper.calculate_area(paper)
area["top"] += header_height
area["bottom"] -= footer_height

pdf = FPDF("portrait", "mm", paper["format"])
pdf.set_auto_page_break(False, 0)
pdf.set_text_color(*rgb.grey)

# Pages
data = pandas.read_csv("data/topics.csv")

for i, row in data.iterrows():
    for j in range(row["Pages"]):
        pdf.add_page()

        # Header
        header_txt = row["Topic"] if not j else ""
        pdf.set_font("Times", "B", header_font)
        pdf.cell(0, header_height, header_txt, 0, 0, "L")

        draw_color = rgb.dark_grey if not j else rgb.white
        pdf.set_draw_color(*draw_color)
        pdf.line(area["left"], area["top"], area["right"], area["top"])

        # Footer
        pdf.ln(area["bottom"] - area["top"] + header_height)
        footer_txt = row["Topic"] + " (cont.)" if j else row["Topic"]
        pdf.set_font("Times", "I", footer_font)
        pdf.cell(0, footer_height, footer_txt, 0, 0, "R")

# Output File
pdf.output("files/python-study-notebook.pdf")
