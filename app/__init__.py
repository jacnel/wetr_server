from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    encodedImage = request.form['encoded_image']
    return "Succeed;" + encodedImage

if __name__ == "__main__":
    app.run()
