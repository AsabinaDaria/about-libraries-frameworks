from flask import Flask

app = Flask(__name__)


@app.route('/')
def f():
    return """<!doctype html>
                <html>
                  <head>
                    <meta charset="utf-8">
                    <title>First</title>
                  </head>
                  <body>
                    <h1>Hello flask</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html>
                <body>
                <h1>А вот ты уже и на другом сайте, дружок!</h1>
                 <div class="alert alert-primary" role="alert">
                 Согласно опросу, опрошенным больше импонирует:
                 <li>tkinter для создания графического дизайна;</li>
                 <li>dash для веб-разработки;</li>
                 <li>pygame для создания игр)))</li>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')