from flask import Flask, render_template
app = Flask(__name__)#template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return "kur"


@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()