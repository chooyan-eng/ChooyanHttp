import socket

class ChooyanHttpClient:

    def request(host, port=80):
        response = ChooyanResponse()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        return response

class ChooyanResponse:
    def __init__(self):
        self.responce_code = None
        self.body = None

if __name__ == '__main__':
    resp = ChooyanHttpClient.request('www.hasam.jp', 80)
    if resp.responce_code == 200:
        print(resp.body)
