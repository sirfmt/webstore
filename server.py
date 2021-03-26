from functools import wraps
import json
import app
from os import environ as env
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from functools import wraps

app = Flask(__name__)

oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='yEYjVmxbrk2deqBpXUTLaZpujNcfE99I',
    client_secret='L8yAgO7NvqHi8a_j_gpUyB3gJSmKRT2mqc4K26b3am2wBERSGjU3yksi4yDcg35n',
    api_base_url='https://dev-pqotmi3e.us.auth0.com',
    access_token_url='https://dev-pqotmi3e.us.auth0.com/oauth/token',
    authorize_url='https://dev-pqotmi3e.us.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)

# Here we're using the /callback route.
@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/dashboard')


@app.route('/login')
def login():
    #_CALLBACK_URL
    return auth0.authorize_redirect(redirect_uri='http://localhost/5000/callback')


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated


@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))

@app.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': 'yEYjVmxbrk2deqBpXUTLaZpujNcfE99I'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))