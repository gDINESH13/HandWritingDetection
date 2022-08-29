from flask import Flask,render_template,request,redirect
#
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
#
# from tensorflow.k

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method == "POST":
        print(request.files['image'])
        img = Image.open(request.files['image'].stream).convert("L")
        img = img.resize((28,28))
        imgToArr = np.array(img)
        imgToArr = imgToArr.reshape(1,28,28,1)
        pred = model.predict([imgToArr])
        print(pred)

        y_pred = np.argmax(pred,axis=1)
        print("The image is "+str(y_pred))
        return redirect('/')
    if request.method=="GET":
        return render_template('web.html')


if __name__=="__main__":
    model = load_model('D:/IBM-naliya Thiran/HandWritingDetection/models/mnistCNN.h5')
# Show the model architecture
    app.run(debug=True)
