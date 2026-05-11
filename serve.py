import http.server, os
os.chdir('/Users/remy/Documents/Pro')
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=3456, bind='')
