from flask import Flask, render_template, send_file
from back_end import parts_template as p_tem
#Creates a Flask Aplication, name app
app = Flask(__name__)

@app.route('/index/')
def index():
    tst = p_tem.hello_world()
    return render_template('index.html')

#run the aplication
if __name__ == "__main__":
    app.run(debug=True)