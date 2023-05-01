from flask import Flask, render_template, request, abort
import os
# from yolo import process
from deoldify_main import process

app = Flask(__name__)


@app.route("/")
def index(name=None):
    return render_template(
        'index.html',
        title="Image Colorization Application ",
        description="Bringing Life and Colors to Your Memories: Image Colorization Made Easy!"
    ) 


@app.route('/upload', methods=['POST'])
def upload_image():
    url = request.args.get('source_url')
    
    try:
        if not url:
            file = request.files['file']
            file.save('test_images/image.png')
            process()
        else:
            process(str(url))
        file_name = "image.png"
        return render_template('index.html', file_name=file_name, 
        title="Image Colorization Application ",
        description="Bringing Life and Colors to Your Memories: Image Colorization Made Easy!")
    except Exception as e:
        print(str(e))
        abort(500)
    
# custom error page for status code 500
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500