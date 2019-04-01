#!/usr/bin/env python
# coding: utf-8

VERSION = "0.1"

logo = """
  _____       _           _    _____                 
 |  __ \     | |         | |  / ____|                
 | |__) |___ | |__   ___ | |_| (___   ___ __ _ _ __  
 |  _  // _ \| '_ \ / _ \| __|\___ \ / __/ _` | '_ \ 
 | | \ \ (_) | |_) | (_) | |_ ____) | (_| (_| | | | |
 |_|  \_\___/|_.__/ \___/ \__|_____/ \___\__,_|_| |_|
                                                     
  Ver %s

""" % VERSION

import os
import site
import handlers.main
from tornado import web
from tornado import ioloop
from tornado import template
from tornado.options import define,options
from libs import output

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write('helloworld')


def main():
    define("port", default=8888, type=int, help='web server port')
    define("address", default='0.0.0.0', help='web server port')
    options.parse_command_line()

    path = lambda root, *a: os.path.join(root, *a)
    ROOT = os.path.dirname(os.path.abspath(__file__))
    settings = {}
    settings['static_path'] = path(ROOT,"static")
    settings['template_loader'] = template.Loader(path(ROOT, "templates"))
    settings['login_url'] = "/login"
    settings['debug'] = False
    site.addsitedir(path(ROOT, 'handlers'))

    url_patterns = [
        (r"^/$", handlers.main.IndexHandler),
        (r"^/index/$", handlers.main.IndexHandler),
        (r"^/scan/$", handlers.main.ScanHandler),
        (r"^/task/$", handlers.main.TaskHandler),
        (r"^/vul/$", handlers.main.VulHandler),
        (r"^/part/$", handlers.main.PartHandler),
        (r"^/report/$", handlers.main.ReportHandler),
    ]
    app=web.Application(url_patterns, **settings)
    app.listen(port=options.port,address=options.address)
    output.good("Web start at: http://%s:%s" % (options.address, options.port))
    ioloop.IOLoop.current().start()

if __name__=='__main__':

    print(logo)
    main()