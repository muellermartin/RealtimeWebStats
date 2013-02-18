import time
import psutil
from ws4py.client.threadedclient import WebSocketClient

class SysMon(object):
	def __init__(self, host):
		self.running = False
		self.client = SysMonWebSocketClient(host)
		self.client.connect()

	def run(self):
		try:
			self.running = True
			i = 1

			while self.running:
				if self.client.terminated:
					print "Loop cycles: %s" % i
					break

				self.client.send(str(psutil.cpu_percent(interval=1)))

				time.sleep(0.15)
				i += 1

		finally:
			self.terminate()

	def terminate(self):
		self.running = False

		if not self.client.terminated:
			self.client.close()
			self.client._th.join()
			self.client = None

class SysMonWebSocketClient(WebSocketClient):
	def opened(self):
		print "opened"

	def received_message(self, message):
		#print message.data
		pass

	def closed(self, code, reason=None):
		print code, reason

if __name__ == "__main__":
	sysmon = SysMon(host="ws://127.0.0.1:9000/ws")

	try:
		sysmon.run()

	except KeyboardInterrupt:
		sysmon.terminate()
