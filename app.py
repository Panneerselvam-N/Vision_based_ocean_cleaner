from flask import Flask,render_template,redirect,request,url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


MODEL_PATH="model/model.h5"
CLASSES1 = ['Waste','Non-waste']
CLASSES2 = ['Combined','Fish','Person','Plastics','Ship','Tyres','Woods']
model= load_model(MODEL_PATH)

def predict(file_name):
    img=image.load_img(file_name,target_size=(224,224))
    img= image.img_to_array(img)
    img= img/255.0
    img= np.expand_dims(img,axis=0)

    
    result = model.predict(img)

    output=result.argmax()

    return output


app=Flask(__name__)
UPLOAD_FOLDER ="static"
@app.route("/",methods=["GET","POST"])
def upload():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_loc = os.path.join(UPLOAD_FOLDER,image_file.filename)
            image_file.save(image_loc)
            ans = predict(image_loc)
            if((ans==1) or (ans==2) or (ans==4)):
                return render_template("index.html",Category= CLASSES1[1],Type=CLASSES2[ans],img_loc=image_loc)
            else:
                return render_template("index.html",Category= CLASSES1[0],Type=CLASSES2[ans],img_loc=image_loc)
            
    return render_template("index.html",Category="Please choose Input Image",img_loc=None)

if __name__ == "__main__":
    app.run()
