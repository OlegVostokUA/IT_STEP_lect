import tornado.ioloop
import tornado.web
from tornado.httputil import HTTPServerRequest


class UploadHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("upload.html")

    def post(self):
        # Handling file uploads
        file_info = self.request.files.get("file_upload")

        if file_info:
            file_content = file_info[0]["body"]
            file_name = file_info[0]["filename"]

            # Set the appropriate Content-Type header for images
            self.set_header("Content-Type", "image/jpeg")

            # Write the binary data directly to the response
            self.write(file_content)
        else:
            self.write("No file uploaded.")


def make_app():
    return tornado.web.Application([
        (r"/upload", UploadHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running at http://localhost:8888/")
    tornado.ioloop.IOLoop.current().start()
