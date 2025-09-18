from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        src_lang = request.form["src_lang"]
        tgt_lang = request.form["tgt_lang"]

        result = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
        translated_text = result

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
