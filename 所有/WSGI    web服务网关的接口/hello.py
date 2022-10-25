def application (enciron, start_response):
    start_response('200 OK', [('Content_Type', 'text/html')])
    body ='<h1>Hello, %s!</h1>' %(enciron['PATH_INFO'][1:] or 'web')

    return [body.encode('utf-8')]
