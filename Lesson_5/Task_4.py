import googl
with open("text_4.txt", "r", encoding="utf-8") as f:
    if f.mode == "r":
        content = f.read()
        print(content)
from googletrans import Translator
translator = Translator()
result = translator.translate(content, src="en", dest="ru")
print(result.text)
