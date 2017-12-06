from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = ' '
    bmi = 0.0
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        weight = request.form.get('weight')
        height = request.form.get('height')

        bmi = float(weight) / float(height)**2

    return render_template("index.html",
                           name=name,
                           bmi=bmi)


if __name__ == '__main__':
    app.run()
