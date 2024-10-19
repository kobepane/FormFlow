from PIL import Image



def text_extract(FILE: Image.Image) -> list[str]:
    
    return ["1", "2", "3", "4", "5", "6", "7", "8"]


# this is what runs when the text extraction is needed
def run_text_extract(FILE: Image.Image) -> list[str]:
    if FILE:
        res: list[str] = text_extract(FILE)
    else:
        return FileNotFoundError()
    # return res
    return NotImplementedError()