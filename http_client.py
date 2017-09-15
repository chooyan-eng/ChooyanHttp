import socket

class ChooyanHttpClient:

    def request(host, port=80):
        response = ChooyanResponse()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        request_str = 'GET / HTTP/1.1\nHost: %s\r\n\r\n' % (host)
        s.send(request_str.encode('utf-8'))
        response = s.recv(4096)

        return response

class ChooyanResponse:
    def __init__(self):
        self.responce_code = None
        self.body = None

if __name__ == '__main__':
    resp = ChooyanHttpClient.request('www.hasam.jp', 80)
    if resp.responce_code == 200:
        print(resp.body)
