from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# On créer le dossier si uploads n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    message = ''
    if request.method == "POST":
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            message = f"File {file.filename} uploaded successfully!"
    return render_template('upload.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)