import config

class form:
    def __init__(self, data: list[str]):
        self.data = data
        
    
    def cut_front(self):
        pass

    def clean_phone(self):
        pass
    
    # email_header = config.CSV_HEADERS[4]
    def clean_email(self):
        result = []
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
                    
                    result.append(full_email) 
        return result

def run_clean(data: list[str]) -> list[str]:
    form_instance = form(data)  # Create an instance of the form class
    return form_instance.clean_email()  # Call clean_email on the instance
