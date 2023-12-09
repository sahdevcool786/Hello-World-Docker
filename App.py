from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return '<h1> Hello-World </h1>'
@app.route("/try",method=['GET'])
def fun():
  return '<h1> Working </h1>'

if __name__ == '__main__':
  app.run(dbug=True,port=5000)
