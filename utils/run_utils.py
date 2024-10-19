from utils import preprocessing
from utils import text_extraction

# run takes a PDF file from the API section. It returns a list of information in order to the API section.
def run(FILE pdf):
    do_prepocessing()
    do_text_extract()
