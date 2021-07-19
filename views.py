from flask import Flask, json, request, jsonify,  render_template, redirect
import os 
import urllib.request
from werkzeug.utils import secure_filename

app =  Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    return 'Home'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["TXT","PDF","DOCX","JPEG", "JPG", "PNG", "GIF"]

def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

                print("File saved : " + filename)

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)
    return render_template("upload_file.html")
if __name__ == '__main__':
    app.run(debug=True)