#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# we need to create app in global layout

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req=request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    res=webhookresult(req)
    res=json.dumps(res, indent=4)
    r= make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def webhookresult(req):
    if req.get("result").get("action") == "BankInterest":
        res=req.get("result")
        parameters=res.get("parameters")
        name=parameters.get("bankname")
        interest={'HDFC':'10.99','ICICI':'11.0','SBI':'11.5'}
        speech="The interest rate of "+name+" is "+str(interest[name])
        return{
            'speech': speech,
            'dispalyText': speech,
            'source': 'BankInterestApp',
        }
    elif req.get("result").get("action") == "MinBalanceDetails":
        res=req.get("result")
        parameters=res.get("parameters")
        name=parameters.get("bankname")
        minbalance={'HDFC':'5000','SBI':'1000','ICICI':'10000'}
        speech="The minimum balance amount for "+name+" is "+str(minbalance[name])
        return{
            'speech':speech,
            'displayText':speech,
            'source':'BankMinbalance details app'
            }
    elif req.get("result").get("action") == "Createincident":
        url = 'https://dev34996.service-now.com/api/now/table/incident'
        # Eg. User name="admin", Password="admin" for this code sample.
        user = 'admin'
        pwd = 'Thrill@4a4'
        # Set proper headers
        headers = {'Content-Type':'application/json','Accept':'application/json'}
        #data='{\"short-description\":\"sample incident from chatbot api\"}'
        # Do the HTTP request
        response = requests.post(url, auth=(user, pwd), headers=headers)
        # Check for HTTP codes other than 201
        if response.status_code != 201:
            resul='failed'
            return resul
        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        incident=data.get("result").get("number")
        return{
            'speech':incident,
            'displayText':incident,
            'source':'Service Now Integration App'
            }
    else:
        return{}
if __name__ == '__main__':
    port=int(os.getenv('PORT', 5000))
    print("App is running on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
