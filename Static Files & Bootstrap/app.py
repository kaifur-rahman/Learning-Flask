from flask import Flask,render_template

#similar to template folder
#mention static folder name and its url path
app=Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/")

@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)