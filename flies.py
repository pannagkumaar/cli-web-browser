import socket
import urllib.parse
import re

def handle_request(request):
    method, path, version = request.split('\r\n')[0].split()
    path = path.lstrip('/')

    if not path:
        path = 'index.html'

    if path.startswith('http'):
        url = path
    else:
        url = f'http://localhost:8000/{path}'

    with urllib.request.urlopen(url) as response:
        content = response.read().decode(errors='ignore')

    # Find all links in the HTML response body
    links = re.findall(r'href=[\'"]?([^\'" >]+)', content)

    # Build an HTML unordered list of links
    links_html = '<ul>\n'
    for link in links:
        if not link.startswith('http'):
            link = f'http://localhost:8000/{link}'
        links_html += f'<li><a href="{link}">{link}</a></li>\n'
    links_html += '</ul>'

    # Build the HTTP response with the HTML unordered list
    response = f'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(links_html)}\r\n\r\n{links_html}'.encode()

    return response

def serve_forever():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(1)

    print('Server is running at http://localhost:8000')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'New client connected: {client_address[0]}:{client_address[1]}')
        request = client_socket.recv(1024).decode()
        print(f'Received request from {client_address[0]}:{client_address[1]}:\n{request}')

        response = handle_request(request)

        client_socket.sendall(response)

        client_socket.close()

if __name__ == '__main__':
    serve_forever()
