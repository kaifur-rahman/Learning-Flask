from flask import Blueprint

feature_bp=Blueprint("feature",__name__)

@feature_bp.route("/feature")
def featureHome():
    return "Welcome to feature homepage"

@feature_bp.route("/feature/details")
def featureDetails():
    return "Welcome to feature details page"