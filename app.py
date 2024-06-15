from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=["GET", "POST"])
def home():
    output = ''
    sentence = ''
    if request.method == "POST":
        sentence = request.form.get("textToTranslate")
        language = request.form.get("languageSelect")
        output = translator.translate(sentence, dest=language).text
    return render_template("index.html", output=output, sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
