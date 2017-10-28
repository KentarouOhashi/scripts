#!/usr/bin/env python3
# coding: utf-8
import http.server

server_address = ("", 8000)
handler_class = http.server.SimpleHTTPRequestHandler
simple_server = http.server.HTTPServer(server_address, handler_class)
simple_server.serve_forever()
