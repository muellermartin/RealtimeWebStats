# -*- coding: UTF-8 -*-

import cherrypy
import os.path
from mako.template import Template
from mako.lookup import TemplateLookup
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket

cherrypy.config.update("global.config")
current_dir = os.path.dirname(os.path.abspath(__file__))
lookup = TemplateLookup(directories=["templates"])
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

class WebSocketHandler(WebSocket):
	def received_message(self, message):
		cherrypy.engine.publish("websocket-broadcast", "[server]" + str(message))
		#self.send("[server] " + message.data, message.is_binary)
		pass

	#def closed(self, code, reason="A client left the room without a proper explanation."):
		#cherrypy.engine.publish("websocket-broadcast", reason)
		#pass

class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		tmpl = lookup.get_template("index.html")
		return tmpl.render(name="Martin")

	@cherrypy.expose
	def ws(self):
		# you can access the class instance through
		handler = cherrypy.request.ws_handler

cherrypy.tree.mount(HelloWorld(), '/', "app.config")

if __name__ == "__main__":
	if hasattr(cherrypy.engine, 'block'):
		# 3.1 syntax
		cherrypy.engine.start()
		cherrypy.engine.block()
	else:
		# 3.0 syntax
		cherrypy.server.quickstart()
		cherrypy.engine.start()
