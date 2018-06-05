import json
import logging

from flask import Flask, g,jsonify
from flask_oidc import OpenIDConnect
import requests

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'Example1',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
    'OIDC_RESOURCE_SERVER_ONLY'

})

oidc2 = OpenIDConnect(app)

@app.route('/api')
@oidc2.accept_token()
def my_api():
     if oidc2.user_loggedin:
        print("loggato %s"%oidc2.user_getfield('preferred_username'))
        print("loggato %s"%oidc2.user_loggedin)
        print ("---> %s"%oidc2.accept_token())
        
        return 'Welcome %s <a href="http://localhost:9000/weather/milan">Tempo</a>' % oidc2.user_getfield('email')

     else:
        return 'Not logged in'



if __name__ == '__main__':
    app.run(debug=True,port=4000)
