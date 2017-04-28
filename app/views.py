from flask import request
from app import app, db, models
from datetime import datetime, timedelta
from app.models import Post
from process_img import process_image
import base64
import cv2
import numpy as np
import traceback

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
    try:
        post = models.Post(name=name, date=date, weight=weight)
        db.session.add(post)
        db.session.commit()
    except Exception as e:
        return str(e)  
    return 'Submitted'

@app.route('/data_request', methods=['POST'])
def data_request():
    try:
        period = request.form['period']        
        if period == "week":
            day1 = str(datetime.utcnow() - timedelta(days=6))
            weights = Post.query.filter(Post.date >= day1).all()
            return str(weights)
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        return str(traceback.format_exception(exc_type, exc_value, exc_traceback))
