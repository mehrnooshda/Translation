from flask import Flask, request, jsonify
import argostranslate.translate



app = Flask(__name__)


@app.route('/translate')
def translate_text():
    from_code = "en"
    to_code = "fa"
    text = request.get_json()["text"]
    # Translate
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = list(filter(
        lambda x: x.code == from_code,
        installed_languages))[0]
    to_lang = list(filter(
        lambda x: x.code == to_code,
        installed_languages))[0]
    translation = from_lang.get_translation(to_lang)
    translated_text = translation.translate(text)
    return jsonify({"result": translated_text}), 200


if __name__ == '__main__':
    app.run(port=8000, debug=True)