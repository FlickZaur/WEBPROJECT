from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/project_flick', methods=['GET'])
def project():
    if request.method == 'GET':
        return render_template('static/teamplates/WEBpr.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
