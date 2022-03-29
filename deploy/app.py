from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask import send_from_directory

app = Flask(__name__,
            static_folder='templates',
            template_folder='templates')

#@app.route("/")
#def index():
#    return render_template('index.html')
    
@app.route('/', defaults=dict(filename=None))
@app.route('/<path:filename>', methods=['GET', 'POST'])
def index(filename):
    filename = filename or 'index.html'
    
    if request.method == 'GET':
        return send_from_directory('.', filename)

    return jsonify(request.data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)