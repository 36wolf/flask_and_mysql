from flask import Flask, render_template, request
import os

app = Flask(__name__,template_folder='./vits_train/templates')

@app.route('/')
def index():
    return render_template('donghua.html')

@app.route('/delete_file', methods=['POST'])
def delete_file():
    file_path = request.form['file_path']
    if os.path.exists(file_path):
        os.remove(file_path)
        return 'File deleted successfully'
    else:
        return 'File not found'

if __name__ == '__main__':
    app.run()
