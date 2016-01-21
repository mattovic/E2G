from flask import Flask

app = (__name__)

@app.route('/auth')
def authenticate():
  return 'Hello world'
  
if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1',port=80)
  
