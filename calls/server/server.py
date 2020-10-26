import cgi
import logging
from service import insert_call
from service import delete_call
from service import get_call

allowed_methods = ['GET', 'POST', 'DELETE']
methodDict = {"POST": insert_call, "DELETE": delete_call, 'GET': get_call}


def app(environ, start_response):
    """The main method, receive all request allowed and redirect to correct service"""
    html = b''
    body = None
    result = None
    if environ['REQUEST_METHOD'] in allowed_methods:
        if environ['REQUEST_METHOD'] == 'POST':
            body = environ['wsgi.input'].peek(1024).decode('utf-8')
        try:
            result = methodDict[environ['REQUEST_METHOD']](body, environ['PATH_INFO'])
        except Exception as err:
            logging.error('The request to not works.', err)
            start_response('500 Internal Server Error', [('Content-Type', 'text/json')])
            html = b'Internal Server Error'
            return [html]
        start_response('200 OK', [('Content-Type', 'text/json')])
        print(result)
        if result:
            return [result.encode()]
        return [html]
    else:
        logging.error('The requested method is not allowed')
        start_response('405 Method Not Allowed', [('Content-Type', 'text/json')])
        html = b'Method Not Allowed'
        return [html]


if __name__ == '__main__':
    """This start cgi server in port 8080, this server a infinite loop"""
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        logging.warning('Started on port 8080....')
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.error('the server not started well.')
