from servidor import SimpleHTTPRequestHandler

def application(environ, start_response):
    handler = SimpleHTTPRequestHandler(None, None, None)
    return handler.handle_request(environ, start_response)