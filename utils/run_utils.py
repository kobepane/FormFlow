from utils import preprocessing
from text_extraction import run_text_extract
from clean_data import *

# run takes a PDF file from the API section. It returns a list of information in order to the API section.
def run(FILE):
    PIL_FILE = do_prepocessing(FILE)
    data = run_text_extract(PIL_FILE)
    res = clean_data(data)
    return res
