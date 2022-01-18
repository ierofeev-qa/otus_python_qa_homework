import socket

from utils import get_open_port, get_request_info, get_request_headers

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    srv_addr = ('', get_open_port())
    print(f'Starting server on {srv_addr}')
    s.bind(srv_addr)
    s.listen(1)

    while True:
        print('Waiting for a connection...')
        conn, raddr = s.accept()

        print('Connection from', raddr)
        while True:
            data = conn.recv(1024)
            text = data.decode('utf-8')

            print(f'Received {repr(text)}')
            if text:
                print('Sending data back to the client...')
                method, status_value, status_name = get_request_info(repr(text))
                request_headers = get_request_headers(repr(text))
                response_data = '\r\n'.join([
                    f"Request Method: {method}<br>",
                    f"Request Source: {raddr}<br>",
                    f"Request Status: {status_value} {status_name}<br>",
                    f"Connection: {request_headers['Connection']}<br>",
                    f"Upgrade-Insecure-Requests: {request_headers['Upgrade-Insecure-Requests']}<br>",
                    f"User-Agent: {request_headers['User-Agent']}<br>",
                    f"Accept: {request_headers['Accept']}<br>",
                    f"Accept-Encoding: {request_headers['Accept-Encoding']}<br>",
                    f"Accept-Language: {request_headers['Accept-Language']}<br>",
                ])
                status_line = f'HTTP/1.1 {status_value} {status_name}'
                headers = '\r\n'.join([
                    status_line,
                    f'Content-Length: {len(response_data)}',
                    'Content-Type: text/html'
                ])

                resp = '\r\n\r\n'.join([
                    headers,
                    f'<h1>{response_data}<h1>'
                ])
                sent_bytes = conn.send(resp.encode('utf-8'))

                print('Data has been sent to the client')
            else:
                print(f'No data from {raddr}')
                conn.close()
                break
