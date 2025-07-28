from flask import Flask,render_template,request

app=Flask(__name__,template_folder="templates")

#handling forms
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=='GET':
        return render_template("index.html")
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if(username=="abc" and password=='abc'):
            return "success"
        else:
            return "Wrong credentials"
#handling files    
@app.route("/file",methods=["POST"])
def fileUpload():
    file=request.files['file']

    if(file.content_type=='text/plain'):
        return file.read().decode()
    else:
        return "Please upload text file"
    
#handling json data
@app.route('/handle-Json',methods=['POST'])
def handlingJson():
    #gets into dict
    data=request.get_json('name')
    print(data)
    return data
app.run(host="0.0.0.0",debug=True)