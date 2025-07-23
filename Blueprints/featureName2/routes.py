from flask import Blueprint,render_template

feature2_bp=Blueprint("feature2",__name__,template_folder="templates")


@feature2_bp.route("/feature2")
def home():
    return "Welcome to feature 2 homepage"

@feature2_bp.route("/feature2/detail")
def details():
    return render_template("index.html")