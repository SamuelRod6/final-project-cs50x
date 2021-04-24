from flask import Flask, render_template, request, flash, redirect

import sys
from googletrans import Translator

# App config
app = Flask(__name__)
app.secret_key = b'_5#y2L"F234n2k3j4Q8z\n\xec]/'

langs = ["Spanish", "English"]

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        result = request.form.get("text").strip()
        in_lang = request.form.get("lang")
        
        if not (in_lang in langs):
            flash("Please, select a valid language.")
            return redirect("/")

        # Translator
        if in_lang == "Spanish":
            out_lang = "en"
        else:
            out_lang = "es"

        t = Translator() 
        t_output = t.translate(result, dest=out_lang)

        translated = str(t_output.text)

        return render_template("translated.html", langs=langs, result=result, translated=translated, in_lang=in_lang)


    else:
        return render_template("index.html", langs=langs)
