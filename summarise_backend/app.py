from flask import Flask, render_template,request,jsonify
import werkzeug
import predictor

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
    # return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
def predict():
    #arr = [int(x) for x in request.form.values()]
    return predictor.recognize()

@app.route("/upload",methods=['POST'])
def upload():
    if(request.method=="POST"):
        imageFile=request.files['image']#image is a key name, which is to be used in the dart file
        filename=werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save("./uploadedImages/"+filename) #try to put one name to be uploaded so that the api can easily accept for predict
        return jsonify({
            "message":"success"
        })
    

if __name__ == "__main__":
    app.run(debug=True)