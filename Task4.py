import re


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        pattern = r'\b[A-Za-z0-9][A-Za-z0-9._-]*@[A-Za-z0-9.-]+\.(?:ru|com|org|net)\b'
        result = re.findall(pattern, self.text)
        return result


input_text = input()
Text = TextProcessor(input_text)
a = Text.extract_emails()
if len(a) == 0:
    print('Не найдено')
else:
    for i in a:
        print(i)



