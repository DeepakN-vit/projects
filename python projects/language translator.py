from googletrans import Translator
 
def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def main():
    input_text = input("Enter the text to translate: ")
    target_language = input("Enter the target language code (Spanish: 'es',French: 'fr',German: 'de',Italian: 'it',Dutch: 'nl',Portuguese: 'pt',Russian: 'ru',Chinese (Simplified): 'zh-CN',Japanese: 'ja',Korean: 'ko',Arabic: 'ar',Hindi: 'hi',Tamil: 'ta'): ")

    translated_text = translate_text(input_text, target_language)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
