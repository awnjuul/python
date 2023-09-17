from module1 import TransLate, LangDetect, CodeLang, LanguageList

def main():
    text_to_translate = "Доброго вечора"

    # Використовуємо функцію TransLate для перекладу тексту
    translated_text = TransLate(text_to_translate, src="uk", dest="en")
    print(f"Перекладенний текст: {translated_text}")

    # Використовуємо функцію LangDetect для визначення мови тексту
    detected_language = LangDetect(text_to_translate, set="lang")
    print(f"Визначена мова: {detected_language}")

    # Використовуємо функцію CodeLang для отримання коду мови
    code = CodeLang("en")
    print(f"Код мови: {code}")

    # Використовуємо функцію LanguageList для виводу списку мов
    result = LanguageList(out="screen", text="Доброго вечора")
    print(result)

if __name__ == "__main__":
    main()