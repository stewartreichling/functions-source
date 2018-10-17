"""Enable a function to respond to HTTP requests.

Converts a function into a Flask app. Incoming requests on the specified port
will cause the function to be invoked.

TODO:
- read module and entrypoint from environment variables
- move invoker.py (and Dockerfile/gunicorn.conf?) to python/
"""


from importlib import import_module
from flask import Flask, request, make_response


FUNCTION_MODULE = 'main'
FUNCTION_ENTRYPOINT = 'hello_http'

def load_user_function(module, entrypoint):
    """Load the user's function and return it to the caller."""
    mod = import_module(module)
    user_func = getattr(mod, entrypoint)
    return user_func


# Load the user's function
user_function = load_user_function(FUNCTION_MODULE, FUNCTION_ENTRYPOINT)

# Create a Flask app that invokes the user's function in response to
# requests on path '/'
app = Flask(__name__)


@app.route('/')
def invoke_user_function():
    """Invoke the user's function."""
    response = user_function(request)
    if not response:
        response = ''
    return make_response(response)
