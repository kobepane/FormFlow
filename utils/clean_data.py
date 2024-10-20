import sys
import os

# Adjust the system path to import config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import GRADE_MAP

class Form:
    def __init__(self, data: list[str]):
        self.data = data  # Initialize with provided data
        self.res = []

    def cut_front(self):
        # Implement this method if needed
        pass

    def clean_phone(self):
        in_word: bool = False
        saved: str = ""

        if not self.data:
            return False

        for i in range(len(self.data)):
            curr: str = self.data[i]
            if curr == "PHONE":
                in_word = True
                continue
            
            if in_word:
                if curr == "MAJOR(S)":
                    self.res.append(saved.strip())
                    return 
                saved += curr + " "  # Accumulate the phone number

    def clean_majors(self):
        in_word: bool = False
        saved: str = ""

        if not self.data:
            return False

        for i in range(len(self.data)):
            curr = self.data[i]
            if curr == "MAJOR(S)":
                in_word = True
                continue
            
            if in_word:
                if curr == "EMAIL":
                    self.res.append(saved.strip())
                    return
                if len(saved) > 0:
                    saved += "/" + curr
                else:
                    saved += curr

    def clean_year(self):
        in_word: bool = False
        saved: str = ""

        if not self.data:
            return False

        for i in range(len(self.data)):
            curr = self.data[i]
            if curr == "YEAR":
                in_word = True
                continue
            
            if in_word:
                if curr == "DATE SIGNED":
                    year = saved.strip()
                    if year in GRADE_MAP:
                        self.res.append(GRADE_MAP[year])
                    else:
                        self.res.append(year)
                    return
                saved += curr + " "  # Accumulate the year

def run_clean(data: list[str]) -> list[str]:
    return NotImplementedError()

if __name__ == "__main__":
    test_data = [
        "PHONE", "5108218486",
        "MAJOR(S)", "Computer Science", "Mathematics",
        "EMAIL", "john@example.com",
        "YEAR", "3",  # Year
        "DATE SIGNED", "01/01/2024"
    ]

    test_form = Form(test_data)
    test_form.clean_phone()
    test_form.clean_majors()
    test_form.clean_year()
    
    # Check the results
    expected_phone = "5108218486"
    expected_majors = "Computer Science/Mathematics"
    expected_year = "Junior"
    
    # Assertions
    assert expected_phone == test_form.res[0]
    assert expected_majors == test_form.res[1]
    assert expected_year == test_form.res[2]

    print(f"Expected Phone: {expected_phone}, Got: {test_form.res[0]}")
    print(f"Expected Majors: {expected_majors}, Got: {test_form.res[1]}")
    print(f"Expected Year: {expected_year}, Got: {test_form.res[2]}")
