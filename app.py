#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# we need to create app in global layout

app = Flask(__name__);

@app.route('/webhook', methods=["POST"])
def webhook():
    req=request.get_json(silent=True, force=True)
    req=json.dumbs(req,indent=4)
    res=webhookresult(req)
    res=json.dumps(res,indent=4)
    r=make_respone(res)
    r.headers('Content-Type')='application/json'
    return r
def webhookresult(req):
    if req.get("result").get("action") != "BankInterest"
      return{}
    res=req.get("result")
    parameters=res.get("parameters")
    name=parameters.get("bankname")
    interest={'HDFC':'10.99','ICICI':'11.0','SBI':'12','AXIS':'11.5'}
    speech="The interest rate of "+name+" is "+str(interest(name))
    return{
      "speech":speech,
      "displayText":speech,
      "source":"bankinterestapp"
    }
  
  if __name__ == '__main__'
     port=int(os.getenv('PORT',5000))
     print("App running on port %d" %(port))
     app.run(debug=false, port=port, host='0.0.0.0')
    
