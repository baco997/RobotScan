#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("index.html")

class ScanHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("scan.html")

class TaskHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("tasks.html")

class VulHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("vuls.html")

class PartHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("parts.html")

class ReportHandler(tornado.web.RequestHandler):

    def get(self):
        return self.render("report.html")