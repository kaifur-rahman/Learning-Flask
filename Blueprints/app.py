from flask import Flask

#import blueprint file which contains routes
from featureName.routes import feature_bp
from featureName2.routes import feature2_bp


#add template folder name here
app=Flask(__name__)

#link that blue print to app here 
app.register_blueprint(feature_bp)
app.register_blueprint(feature2_bp)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002,debug=True)