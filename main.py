from google import genai
from flask import Flask,request,render_template

client=genai.Client(api_key='AIzaSyBhuvXo4ODnxXPRYPgImr6buXdI-LWtxnw')
app=Flask(__name__)
@app.route("/")
def home():
   return render_template('index.html')
# def hello_world():
#     return "<p>Hello, World!</p>"
# @app.route("/cart")
# def hello_world():
#     return "<p>CART</p>"
@app.route("/chat",methods=["POST"])
def chat():
  return client.models.generate_content(
    model='gemini-2.5-flash',
    contents=request.json["msg"]
).text

app.run(port=5001)

if __name__=="__main__":
    app.run(debug=True,port=5001)