import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.clean_data import *

def test_clean_phone():
    test_form = Form(["PHONE", "5108218486", "MAJOR(S)"])
    test_form.clean_phone()
    expected = "5108218486"
    assert expected == test_form.res[0]


if __name__ == "__main__":
    test_clean_phone()