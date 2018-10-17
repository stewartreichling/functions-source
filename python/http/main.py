"""A starter HTTP function.

Get started by editing the code in the `hello_http` function. This HTTP
function is based on the Flask microframework <http://flask.pocoo.org/>.
"""

def hello_http(request):
    """Function that responds to an HTTP request.

    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#incoming-request-data>.
    Returns:
        Any set of values that can be convert to a Response object using
        Flask's `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.make_response>.

    """
    return 'Hello, World!'