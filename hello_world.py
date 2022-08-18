
async def app(scope, receive, send):
    with open('index.html') as index:
        body = index.read()
        if scope["type"] != "http":
            raise Exception("Only the HTTP protocol is supported")

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                (b'content-type', b'text/html;charset=utf-8'),
            ],
        })
        
        await send({
            'type': 'http.response.body',
            'body': bytes(body, 'utf-8'),
        })

