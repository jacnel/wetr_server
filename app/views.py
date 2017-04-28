from flask import render_template, request, url_for
from app import app, db
from datetime import datetime
from app.models import Post
from process_img import process_image
import io
import base64
import cv2
import numpy as np
import PIL
import traceback

@app.route('/process_img', methods=['POST'])
def process():
    try:
        data = request.form['encoded_image']
        
        decoded = base64.b64decode(data)
        im = np.fromstring(decoded, dtype=np.uint8)
        cv2_img = cv2.imdecode(im, 1)
        try:
            return process_image(cv2_img)
        except Exception as e:
            return "in process_image()" + str(e)
    except Exception as e:
        return str(e)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    date = datetime.utcnow()
    weight = request.form[weight]

    post = Post(name, date, weight)
    db.session.add(post)
    db.session.commit()
    return 'Submitted'
