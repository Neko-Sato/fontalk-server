from main import app

if __name__ == '__main__':
    #import ssl
    #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #context.load_cert_chain('server.crt', 'server.key')

    app.run(\
        debug=False, \
        #ssl_context=context, \
        host='localhost', \
        port=5000, \
    )