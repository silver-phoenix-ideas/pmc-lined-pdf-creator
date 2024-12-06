def get_paper(paper_format: str = "A4"):
    paper_format = paper_format.casefold()

    paper = {
        "format": paper_format,
        "margin_top": 10,
        "margin_right": 10,
        "margin_bottom": 20,
        "margin_left": 10
    }

    match paper_format:
        case "a3":
            paper["width"] = 297
            paper["height"] = 420
        case "a4":
            paper["width"] = 210
            paper["height"] = 297
        case "a5":
            paper["width"] = 148
            paper["height"] = 210
        case "letter":
            paper["width"] = 216
            paper["height"] = 279
        case "legal":
            paper["width"] = 216
            paper["height"] = 356
        case _:
            paper["width"] = 0
            paper["height"] = 0

    return paper


def calculate_area(paper):
    area = {
        "top": paper["margin_top"],
        "bottom": paper["height"] - paper["margin_bottom"],
        "left": paper["margin_left"],
        "right": paper["width"] - paper["margin_right"]
    }

    return area


def draw_area(pdf, area, color):
    pdf.set_draw_color(*color)

    # Top Line
    pdf.line(area["left"], area["top"], area["right"], area["top"])

    # Bottom Line
    pdf.line(area["left"], area["bottom"], area["right"], area["bottom"])

    # Left Line
    pdf.line(area["left"], area["top"], area["left"], area["bottom"])

    # Right Line
    pdf.line(area["right"], area["top"], area["right"], area["bottom"])


def draw_horizontal_lines(pdf, area, step, color):
    pdf.set_draw_color(*color)

    for y in range(area["top"] + step, area["bottom"], step):
        pdf.line(area["left"], y, area["right"], y)


def draw_vertical_lines(pdf, area, step, color):
    pdf.set_draw_color(*color)

    for x in range(area["left"] + step, area["right"], step):
        pdf.line(x, area["top"], x, area["bottom"])


def draw_grid(pdf, area, step, color):
    draw_horizontal_lines(pdf, area, step, color)
    draw_vertical_lines(pdf, area, step, color)
