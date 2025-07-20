from flask import Flask,render_template

#add template folder name here
app=Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    #just enter location inside templates folder
    return render_template("index.html")

#passing dynamic value to html
@app.route("/dynamic")
def dynamic():
    arr=[10,20,30,40,"check"]
    return render_template("dynamic.html", values=arr)

#creating a filter for template
@app.template_filter('reverseString')
def reverse(s):
    return s[::-1]

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002,debug=True)