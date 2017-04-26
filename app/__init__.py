from flask import Flask, render_template, request, url_for
from process_img import process_image
import io
import base64
import cv2
import numpy as np
import PIL
import traceback

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    try:
        data = request.form['encoded_image']
        im = np.frombuffer(base64.b64decode(data), dtype=np.uint8)
        cv2_img = cv2.imdecode(im, 1)
        return process_image(cv2_img)
    except Exception as e:
        return str(e)

 
if __name__ == "__main__":
    app.run()
