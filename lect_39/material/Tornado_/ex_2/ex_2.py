import tornado.ioloop
import tornado.web

class FormHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

	def post(self):
		name = self.get_argument("name")
		self.write(f"Hello, {name}!")

def make_app():
	return tornado.web.Application([(r"/form", FormHandler)])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
