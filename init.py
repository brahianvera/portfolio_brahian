from flask import Flask, render_template, send_file
#Creates a Flask Aplication, name app
app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')

#run the aplication
if __name__ == "__main__":
    app.run(debug=True)