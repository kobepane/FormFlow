import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import START_KEYWORD

class Form:
    def __init__(self, data: list[str]):
        self.data = self.cut_front(data)
        self.res: list[str] = []
    
    def cut_front(self, data: list[str]) -> list[str]:
        # Look for START_KEYWORD in data, and cut out everything before it
        index = data.index(START_KEYWORD)
        return data[index+1:]

    def clean_phone(self):
        pass

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


def clean_data(data: list[str]) -> list[str]:
    form = Form(data)
    form.clean_name()
    print(form.res)
