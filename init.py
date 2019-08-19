from flask import Flask, render_template, send_file
from back_end import parts_template as p_tem
#Creates a Flask Aplication, name app
app = Flask(__name__, template_folder='templates')

@app.route('/<name_template>', methods=['GET'])
def index(name_template):
    parts_temp = p_tem.parts_templates()
    return render_template( name_template, parts_temp =  parts_temp.all_parts())

#run the aplication
if __name__ == "__main__":
    app.run(debug=True)