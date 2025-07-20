from flask import Flask,request,make_response

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to homepage</h1>"

#response with status code
@app.route("/status-code")
def statusCode():
    return "Status code sent",201

#manipulating other response infos
@app.route("/status-code-adv")
def response():
    response=make_response("<h1>We will put content here</h1>")
    response.status_code=202
    response.headers['content-type']="text/plain"
    return response

#dynamic routes
@app.route("/greet/<name>")
def greetWithName(name):
    return f"Hello <h1>{name}</h1>"

#can specify data type also
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"{a}+{b}={a+b}"

#handling query params
@app.route("/query")
def handlingQueryParams():
    #request.args contains dictionary of query param
    name=request.args.get("name")
    age=request.args.get("age")
    if(age!=None and name!=None):
        return f"Name:{name} Age:{age}"
    else:
        return "Some parameters are missing"
    
#to handle http methods
@app.route("/methods",methods=['GET','POST'])
def methodHandling():
    if (request.method=='GET'):
        return "This is get request"
    elif (request.method=='POST'):
        return "This is post request"
    else:
        return "This is other than get & post request"

if __name__=="__main__":
    app.run("0.0.0.0",port=5000,debug=True)