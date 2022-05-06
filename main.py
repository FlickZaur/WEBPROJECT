from flask import Flask, render_template

app = Flask(__name__)


@app.route('/project_flick')
def project():
    return render_template('WEBpr.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
