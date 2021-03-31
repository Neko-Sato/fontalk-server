from fontalk import app, db
import argparse

db.create_all() 

class MyFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.MetavarTypeHelpFormatter):
    pass

parser = argparse.ArgumentParser(
  prog='run.py',
  formatter_class=MyFormatter, 
  usage='python %(prog)s [options]', 
  description='\
    2021年度 新宿山吹高校 情報科2部7組 清水 一聡\
    このプログラムは 課題研究②ｱ の作品になります。\
  ',
  epilog='Copyright © 20021 Hisatshi Shimizu All Rights Reserved.',
  add_help=True,
)
parser.add_argument(
  "-b",
  "--bind",
  dest="address",
  default="localhost:5000",
  type=str, 
  help="The hostname:port the app should listen on.",
)
parser.add_argument(
  "-d",
  "--debug",
  dest="use_debugger",
  action="store_true",
  default=False,
  help="Use Werkzeug's debugger.",
)
parser.add_argument(
  "-r",
  "--reload",
  dest="use_reloader",
  action="store_true",
  default=False,
  help="Reload Python process if modules change.",
)

if __name__ == '__main__':
  args = vars(parser.parse_args())
  options = {}
  if args['address']:
    address = args['address'].split(":")
    args['host'] = address[0]
    if len(address) > 1:
      args['port'] = address[1]
    del address
  del args['address']
  args.setdefault('host')
  args.setdefault('port')

  #import ssl
  #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
  #context.load_cert_chain('server.crt', 'server.key')
  #options.update(ssl_context=context)

  #app.run(**args, **options)