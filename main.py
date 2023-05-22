
from deep_translator import GoogleTranslator
import json


def translate_texts(texts, target_lang):
    translations = {}
    for text in texts:
        translations[text] = GoogleTranslator(source='en', target=target_lang).translate(text)

    return translations


def main():
    # Read texts from file
    with open('phrases.txt', 'r', encoding='utf-8') as file:
        english_texts = [line.strip() for line in file.readlines()]

    # Translate English texts to Swahili
    swahili_translations = translate_texts(english_texts, "sw")
    # Translate English texts to French
    french_translations = translate_texts(english_texts, "fr")
    # Translate English texts to Spanish
    spanish_translations = translate_texts(english_texts, "es")

    # Group translations into JSON objects
    swahili_json = json.dumps({text: translation for text, translation in swahili_translations.items()},
                              ensure_ascii=False)
    french_json = json.dumps({text: translation for text, translation in french_translations.items()},
                             ensure_ascii=False)
    spanish_json = json.dumps({text: translation for text, translation in spanish_translations.items()},
                              ensure_ascii=False)

    # Create JSON object with English texts as keys and values
    english_json = json.dumps({text: text for text in english_texts})

    # Print the JSON objects
    print("English Texts:")
    print(english_json.replace('", "', '",\n"'))
    print("\nSwahili Translations:")
    print(swahili_json.replace('", "', '",\n"'))
    print("\nFrench Translations:")
    print(french_json.replace('", "', '",\n"'))
    print("\nSpanish Translations:")
    print(spanish_json.replace('", "', '",\n"'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
