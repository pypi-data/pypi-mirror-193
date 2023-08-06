import fastapi, uvicorn, threading

from . import Connection



class Server:
	# TODO implement some security maybe

	def __init__(self, port: int, log=False):
		"""Open this device for connections"""
		self.port = port
		self.fastapi = fastapi.FastAPI()

		if log:
			log_level = None
		else:
			log_level = 'warning'
		self.uvicorn = uvicorn.Server(uvicorn.Config(self.fastapi, host='0.0.0.0', port=self.port, log_level=log_level))
		self.uvicorn_thread = threading.Thread(target=self.uvicorn.run, daemon=True)

		self.connections: set[Connection] = set()

		@self.fastapi.post('/connect')
		def add_client(port: int, request: fastapi.Request):
			client = Connection(request.client.host, port, self.port)
			if client not in self.connections:
				self.connections.add(client)
				client.connect()

		@self.fastapi.post('/disconnect')
		def remove_client(port: int, request: fastapi.Request):
			client = Connection(request.client.host, port, self.port)
			if client in self.connections:
				self.connections.remove(client)
				client.disconnect()


		@self.fastapi.get('/test')
		def hello():
			return "Hello!"

		@self.fastapi.exception_handler(Exception)
		async def validation_exception_handler(request, err: Exception):
			return fastapi.responses.JSONResponse(status_code=500,
												  content={'detail': f"{err.__class__.__name__}: {err}"})


	def start(self):
		self.uvicorn_thread.start()

	@property
	def running(self):
		return self.uvicorn.started and self.uvicorn_thread.is_alive()

	def stop(self):
		self.uvicorn.should_exit = True
	#	asyncio.run(self.uvicorn.shutdown())

