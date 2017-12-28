from flask import Flask, render_template, request

from typograf import typograf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():

    source_text = request.form.get('text') or ''
    result_text = '' if source_text == '' else typograf(source_text) 
    return render_template('form.html', source_text=source_text, result_text=result_text)

if __name__ == "__main__":
    app.run()
