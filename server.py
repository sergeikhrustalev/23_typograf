from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():

    if request.method == 'POST':
        result_text = request.form.get('text')
 
        return render_template('form.html', result_text=result_text)

    return render_template('form.html')

if __name__ == "__main__":
    app.run()
