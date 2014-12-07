from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import goslate

class PostHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        translation = ""
        text = form["text"].value
        lang = form["lang"].value
        gs = goslate.Goslate()
        translation = gs.translate(text, lang)

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(translation.encode('utf-8'))

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 1234), PostHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
