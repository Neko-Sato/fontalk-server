from main import app
import argparse

parser = argparse.ArgumentParser(description='説明')
parser.add_argument('--port', type=int, help='ポート')

if __name__ == '__main__':
    args = vars(parser.parse_args())
    for key, value in list(args.items()):
        if value == None:
            del args[key]
    
    #import ssl
    #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    #context.load_cert_chain('server.crt', 'server.key')
    #args.update(ssl_context=context)

    #--Default--
    args.setdefault("debug", False)
    args.setdefault("host", 'localhost')
    args.setdefault("port", 5000)

    app.run(**args)