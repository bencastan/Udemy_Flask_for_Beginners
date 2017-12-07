from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    name = ' '
    bmi = 0.0
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))

        bmi = calc_bmi(weight, height)

    return render_template("index.html",
                           name=name,
                           bmi=bmi)


def calc_bmi(weight, height):
    return round((weight / height ** 2), 2)


if __name__ == '__main__':
    app.run()
