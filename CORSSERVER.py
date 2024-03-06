from http.server import BaseHTTPRequestHandler, HTTPServer
import re 

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('', 80)
  httpd = server_class(server_address, handler_class)
  try: httpd.serve_forever()
  except KeyboardInterrupt: httpd.server_close()

class HttpGetHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        if (self.path=="/user/private-info"):
            Origin = self.headers['Origin']
            self.send_response(204)
            self.send_header("Access-Control-Allow-Methods", "GET")
            self.send_header("Access-Control-Allow-Credentials", "true")
            # ТЕСТ 1. Отражение любого Origin 
            self.send_header("Access-Control-Allow-Origin", Origin)
            # ТЕСТ 2. Некорректный парсер поддомена с доверием http
            # if re.match(r".+olegbrain\.ru$", Origin): self.send_header("Access-Control-Allow-Origin", Origin)
            # else: self.send_header("Access-Control-Allow-Origin", "https://olegbrain.ru")
            # ТЕСТ 3. Некорректный парсер символов на основе стандарта доменных имен
            # if re.match(r"^http(s|)://[a-zA-Z0-9\.-]*$", Origin): self.send_header("Access-Control-Allow-Origin", "https://olegbrain.ru")
            # else: self.send_header("Access-Control-Allow-Origin", Origin)
            self.end_headers()

run(handler_class=HttpGetHandler)






