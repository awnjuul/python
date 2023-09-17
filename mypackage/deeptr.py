from deep_translator import GoogleTranslator
from langdetect import detect

def main():
    text_to_translate = "Добрий вечір"


    translated_text = GoogleTranslator(source="auto", target="en").translate(text_to_translate)
    print(f"Перекладенний текст: {translated_text}")


    detected_language = detect(text_to_translate)
    print(f"Визначена мова: {detected_language}")

if __name__ == "__main__":
    main()