import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import START_KEYWORD
from config import GRADE_MAP

class Form:
    def __init__(self, data: list[str]):
        self.data = self.cut_front(data)
        self.res: list[str] = []
    
    def cut_front(self, data: list[str]) -> list[str]:
        # Look for START_KEYWORD in data, and cut out everything before it
        index = data.index(START_KEYWORD)
        return data[index+1:]
      
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
    
    # email_header = config.CSV_HEADERS[4]
    def clean_email(self):
        words = self.data
        for i, word in enumerate(words):
            joined_word = ''.join(word) if isinstance(word, list) else word
            if joined_word.lower() == "email":
                if i >= 3 and i + 1 < len(words):
                    before = ''.join(words[i-3]) if isinstance(words[i-3], list) else words[i-3]
                    after = ''.join(words[i+1]) if isinstance(words[i+1], list) else words[i+1]
                    
                    # Replace the second occurrence of lowercase 'e' with '@'
                    e_count = 0
                    before_modified = []
                    for char in before:
                        if char == 'e':
                            e_count += 1
                            if e_count == 2:  # Replace on the second occurrence
                                before_modified.append('@')
                                continue
                        before_modified.append(char)
                    
                    beforeAt = ''.join(before_modified)  # Join the modified characters back into a string
                    full_email = beforeAt + after  # Correctly join the beforeAt string and the after string
                    
                    self.res.append(full_email) 
        return

    def run_clean(data: list[str]) -> list[str]:
        form_instance = Form(data)  # Create an instance of the form class
        return form_instance.clean_email()  # Call clean_email on the instance

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


    def clean_date(self):
        start = "SIGNED"
        end = "WORK"
        date = ""
        start_i = 0
        for i in range(len(self.data)):
            word = self.data[i]
            if word == start:
                for j in range(i + 1, len(self.data)):
                    date_part = self.data[j]
                    if date_part == end:
                        self.res.append(date)
                        return
                    
                    if date_part == '':
                        continue

                    if len(date) == 0:
                        date += f"{date_part}"
                    else:
                        date += f"-{date_part}"
    
    def clean_name(self):
        start = "NAME"
        first_name = ""
        last_name = ""
        for i in range(len(self.data)):
            word = self.data[i]
            if word == start:
                first_name = self.data[i + 1]
                last_name = self.data[i + 2]
                break
        
        self.res.append(first_name)
        self.res.append(last_name)
        return

    def clean_org_name(self):
        start = "NAME:"
        org_name = ""
        for i in range(len(self.data)):
            word = self.data[i]
            if word == start:
                for j in range(i + 1, len(self.data)):
                    name_part = self.data[j]

                    if name_part == '':
                        continue

                    if len(org_name) == 0:
                        org_name += name_part
                    else:
                        org_name += f" {name_part}"
                
                break
        
        self.res.append(org_name)
        return
    
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

def clean_data(data: list[str]) -> list[str]:
    form = Form(data)
    form.clean_name()
    form.clean_phone()
    form.clean_majors()
    form.clean_email()
    form.clean_year()
    form.clean_date()
    form.clean_org_name()
    return form.res