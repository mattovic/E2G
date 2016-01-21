from flask import Flask
from flask import request

app = (__name__)

@app.route('/auth')
def authenticate():
  
  token = 'xxxxxx'
  
  signature = request.args.['signature']
  timestamp = request.args.['timestamp']
  nonce = request.args.['nonce']
  echostr = request.args.['echostr']
  
  triplet = sorted([token, timestamp, nonce])
  tmpstr =hash(triplet[1] + triplet[2] + triplet[3])
  
  if (echostr == tempstr):
    return echostr
  else:
    return 'Fuch you'
  
if __name__ == '__main__':
  app.debug = True
  app.run(host='127.0.0.1',port=80)
  
