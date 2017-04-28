from flask import request
from app import app, db
from datetime import datetime
from app.models import Post
from process_img import process_image
import base64
import cv2
import numpy as np

@app.route('/process_img', methods=['POST'])
def process():
 #   with open('/var/www/wetr/temp/result.log', 'w') as f:
    try:
#        return "Success!"
        data = request.form['encoded_image']
        
        decoded = base64.b64decode(data)
        im = np.fromstring(decoded, dtype=np.uint8)
        cv2_img = cv2.imdecode(im, 1)
        try:
            result = process_image(cv2_img)
            if result == '0.0':
                return result
            elif result == '':
                return '0.0'
            else:
                result = result.replace(" ", "")
                result = result.replace(".","*", 1)
                result = result.replace(".","")
                result = result.replace("*",".")
                try:
                    decimal = result.index('.')
                    result = result[0:decimal + 2]
                except Exception as e:
                    pass
                finally:
                    #                        f.write(result)
                    return result
        except Exception as e:
            return "in process_image()" + str(e)
    except Exception as e:
        return str(e)
                        
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    date = datetime.utcnow()
    weight = request.form['weight']

    post = Post(name, date, weight)
    db.session.add(post)
    db.session.commit()
    return 'Submitted'
