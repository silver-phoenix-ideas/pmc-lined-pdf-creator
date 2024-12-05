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
