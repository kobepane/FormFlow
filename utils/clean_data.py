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
