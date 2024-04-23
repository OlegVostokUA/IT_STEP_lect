import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    ### ex 1
    # def get(self):
    #     self.write('<h1>Hello world</h1>')

    ### ex 2
    # def get(self):
    #     self.render('index.html')
    #
    # def post(self):
    #     name = self.get_argument('name')
    #     self.write(f'Hello {name}')

    #### ex 3
    def get(self):
        self.render('upload.html')

    def post(self):
        file_info = self.request.files.get('file_upload')

        if file_info:
            file_name = file_info[0]['filename']
            file_content = file_info[0]['body']

            self.set_header('Content-type', 'image/jpg')

            self.write(file_content)
        else:
            self.write('No file')

class MainHandler2(tornado.web.RequestHandler):
    ### ex 1
    # def get(self):
    #     self.write('<h1>Hello world</h1>')

    ## ex 2
    def get(self):
        self.render('index.html')

    def post(self):
        name = self.get_argument('name')
        self.write(f'Hello {name}')



def make_app():
    return tornado.web.Application([(r'/upload', MainHandler), (r'/form', MainHandler2)])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
