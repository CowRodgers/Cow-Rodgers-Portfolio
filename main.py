from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    return render_template('index.html', year=current_year, month=current_month)


if __name__ == "__main__":
    app.run(debug=True)

