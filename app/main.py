from flask import Flask, render_template, send_from_directory, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, MultipleFileField
from werkzeug.utils import secure_filename
import os
import xml.etree.ElementTree as ET
import shutil
import features

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    files = MultipleFileField("Files")
    submit = SubmitField('Upload File')

class RunMagic(FlaskForm):
    run = SubmitField('Download files')

filenames = []

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        for file in form.files.data:
            filename = secure_filename(file.filename)
            print(filename)
            filenames.append(filename)
            filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

        print('Running Magic')

        for file in filenames:
            # Load the XML file
            filename = secure_filename(file)
            filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename)
            print(filepath)
            features.find_and_replace(filepath)
    
        return redirect('/download')
    return render_template('index.html', form=form)

@app.route('/download', methods=['GET', 'POST'])
def download():
    form2 = RunMagic()
    if form2.validate_on_submit():
        shutil.make_archive('static/zip', 'zip', 'static/files')
        print('downloading')        
        return send_from_directory('static', 'zip.zip', as_attachment=True)

    return render_template('download.html', form=form2)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form2 = RunMagic()
    if form2.validate_on_submit():
        os.remove('static/zip.zip')
        print('deleted zip')
        # shutil.rmtree(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER']))
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER']) + '/'
        for file_name in os.listdir(path):
            # construct full file path
            file = path + file_name
            if os.path.isfile(file):
                print('Deleting file:', file)
                os.remove(file)

        print('deleted files')
        return redirect('/home')
    
    return render_template('delete.html', form=form2)

if __name__ == '__main__':
    app.run(debug=True)