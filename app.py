from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET' , 'POST'])
def index():
    return "hello! starting Machine learning Project"


if __name__=="__main__":
    app.run(debug=True)
    
## willl add this to git after