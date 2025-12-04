from flask import *



APP = Flask(__name__)
APP.secret_key = "my$up3r_S3cr3t_Key_123!"




@APP.route("/")
def HomeAr():
    return render_template("index.html")

@APP.route("/Ar")
def HomeArr():
    return render_template("index.html")



@APP.route("/En")
def HomeEn():
    return render_template("index2.html")




if __name__ == "__main__":
    APP.run(debug=True, port=7000)
    
