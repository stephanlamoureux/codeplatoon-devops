import socket
import datetime
import json


class Request:
    def __init__(self, request_text):
        self.parse_request(request_text.recv(4096).decode("utf-8").split("\r\n"))

    def parse_request(self, decoded_request_text):
        self.parsed_request = {}
        request_line = decoded_request_text[0].split()
        if len(request_line) >= 2:
            self.parsed_request["method"] = request_line[0]
            self.parsed_request["uri"] = request_line[1]


def build_html_response(text_body):
    html_body = f"<html><head><title>An Example Page</title></head><body>{text_body}</body></html>"
    return f"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\nContent-Length:{len(html_body)}\r\n\r\n{html_body}"


def build_json_response(data):
    json_body = json.dumps(data)
    return f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {len(json_body)}\r\n\r\n{json_body}"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)  # so you don't have to change ports when restarting
server.bind(("0.0.0.0", 9292))

while True:
    server.listen()
    print("waiting for a request on localhost:9292")
    client_connection, _client_address = server.accept()
    client_request = Request(client_connection)
    if client_request.parsed_request.get("uri") == "/":
        client_connection.send(build_html_response("Hello World").encode())
    elif client_request.parsed_request.get("uri") == "/time":
        current_time = datetime.datetime.now()
        serialized_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        response_data = {"time": serialized_time}
        client_connection.send(build_json_response(response_data).encode())
    client_connection.close()
