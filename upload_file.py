from flask import Flask, json, request, jsonify,  render_template, redirect
import os 
import urllib.request
from werkzeug.utils import secure_filename
import model_frequency 

app =  Flask(__name__,template_folder='templates')

from dashboard import create_dash_application

create_dash_application(app)

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["ALLOWED_FILE_EXTENSIONS"] = ["TXT","PDF","DOCX","JPEG", "JPG", "PNG", "GIF"]

def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False
@app.route('/')
@app.route("/upload-file/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if request.files:
            file = request.files["file"]

            if file.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_file(file.filename):
                filename = secure_filename(file.filename)

                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

                print("File saved : " + filename)
                frequency_df = model_frequency.frequency_sim().reset_index()
                # headin = frequency_df.columns.values
                # print(headin)
                # print(frequency_df)
                print(frequency_df)
                # print(type(frequency_df))

                # return render_template("table.html", headings=headings, data=data)
                return render_template("table.html", headings=frequency_df.columns.values, data=list(frequency_df.values.tolist()), zip=zip)

                # return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)
    return render_template("upload_file.html")

if __name__ == '__main__':
    app.run(debug=True)