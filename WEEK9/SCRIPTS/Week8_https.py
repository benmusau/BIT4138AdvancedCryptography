import http.server
import ssl

server_address = ('localhost', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="certificate.crt", keyfile="private.key")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server running at https://localhost:4443")
httpd.serve_forever()