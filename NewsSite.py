from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home(): 
	return render_template('home.html')

@app.route("/news")
def News():
    return render_template('NewsSummaries_News.html')

@app.route("/health")
def Health():
    return render_template('NewsSummaries_Health.html')
    
@app.route("/pharma")
def Pharma():
    return render_template('NewsSummaries_Pharma.html')

# @app.route("/Fox")
# def FOX():
#     return render_template('NewsSummaries_Fox.html')  

if __name__ =='__main__':
    app.run(debug=True)
