from flask import Flask, render_template

app = Flask(__name__)

#definindo rota url
@app.route("/inicio")

def ola():
    return render_template('lista.html')
    #vai renderizar meu arquivo html

app.run(host='localhost', port=9999, debug=True)