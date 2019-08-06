from flask import Flask
app = Flask(__name__)


@app.route('/menu')
def hello_world():
    return """<ul>
                    <li>
                        <a href="index.html">Home</a>
                    </li>
                    <li>
                        <a href="about.html" class="active">About</a>
                    </li>
                    <li>
                        <a href="skills.html">Skills</a>
                    </li>
                    <li>
                        <a href="services.html">Services</a>
                    </li>
                    <li>
                        <a href="portfolio.html">Portofolio</a>
                    </li>
                    <li>
                        <a href="contact.html">contact</a>
                    </li>
                </ul>"""