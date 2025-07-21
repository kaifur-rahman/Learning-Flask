from flask import Flask,render_template,session,make_response,request

#similar to template folder
#mention static folder name and its url path
app=Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/")

#for setting session in server side we need to define strong secret_key
app.secret_key="use-strong-key-in-prod"

# note session is a dictonary its key is unique user's session

@app.route("/")
def home():
    nameOfSession=None
    if("name" in session):
        nameOfSession=session["name"]
    if(nameOfSession):
        return render_template("index.html",message=f"Session already going for {nameOfSession}")
    else:
        return render_template("index.html",message="No Existing session found")

#sessions----------------------------------
#route to set session
@app.route("/set-session")
def setSession():
    session['name']="kaifur" 
    return render_template("index.html", message=f"Session has been set for kaifur")

#route to get session
@app.route("/get-session")
def getSession():
    nameOfSession=None
    if("name" in session):# just check if that key exist in session dictionary or not
        nameOfSession=session['name']
    if(nameOfSession):
        return render_template("index.html",message=f"Session retrieved for {nameOfSession}")
    else:
        return render_template("index.html",message="No Session found on server")

#route to clear session
@app.route("/clear-sessin")
def clearSession():
    if("name" in session):
        del session["name"]
        return render_template("index.html",message="Session has been cleared")
    else:
        return render_template("index.html",message="No session found to be cleared")

#Cookies----------------------
#route to set cookie
@app.route("/set-cookies")
def setCookies():
    #we use make_response to manipulate response so that browser can set that cookie
    response=make_response(render_template("index.html",message="Cookies has been set"))
    response.set_cookie("cookie-name","cookie-value")
    return response

#route to get cookie
@app.route("/get-cookie")
def getCookies():
    #we find cookie details in request header
    if('cookie-name' in request.cookies):
        cookie_val=request.cookies['cookie-name']
        return render_template("index.html",message=f"Cookie retrieved value is {cookie_val}")
    else:
        return render_template("index.html",message=f"No cookie found to fetch")
 

#route to clear cookie
@app.route("/clear-cookies")
def clearCookies():
    #note request header is used to get cookie
    if('cookie-name' in request.cookies):
        response=make_response(render_template("index.html",message="Cookie has been cleared"))
        response.delete_cookie("cookie-name")
        return response
    else:
        return render_template("index.html",message="No cookie found to clear")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)