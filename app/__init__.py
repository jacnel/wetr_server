from flask import Flask, render_template, request, url_for
import process_img as pi
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data['img'] = request.form['encoded_image']
    im = PIL.Image.open(io.BytesIO(base64.b64decode(data)))
    cv2_img = np.array(im)

    small_gray_img = preproc(cv2_img)
    filtered_edged_img = filter_and_edge(small_gray_img)
    display_contours = contour_and_extract_norm_display(img, filtered_edged_img)
    warped_display = warp_perspective(img, display_contours)
    ocr_value = proc_with_tesseract(warped_display)

    return "Succeed;" + ocr_value

if __name__ == "__main__":
    app.run()
