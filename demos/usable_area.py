# Imports
from fpdf import FPDF
import modules.color_palette as rgb
import modules.pdf_helper as pdf_helper

# Document
paper = pdf_helper.get_paper("A4")
area = pdf_helper.calculate_area(paper)
pdf = FPDF("portrait", "mm", paper["format"])

# Page
pdf.add_page()
pdf_helper.draw_area(pdf, area, rgb.black)

# Output File
pdf.output("../files/demo-usable-area.pdf")
