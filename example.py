from flask import Flask
from flask import request

app = (__name__)

@app.route('/auth')
def authenticate():
  
  token = 'xxxxxx'
  
  signature = request.args.get('signature')
  timestamp = request.args.get('timestamp')
  nonce = request.args.get('nonce')
  echostr = request.args.get('echostr')
  
  triplet = [token, timestamp, nonce]
  triplet.sort()
  tmpstr =hash(triplet[1] + triplet[2] + triplet[3])
  
  if (echostr == tempstr):
    return echostr
  else:
    return 'Fuch you'
  
if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1',port=80)
  
