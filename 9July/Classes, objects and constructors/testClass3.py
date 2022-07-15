import logging

class logs:
    def __init__(self, filename, level, format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename, level= self.level,format=self.format)

    def log(self, message, method):
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)

class Blogs:
    def __init__(self):

        self.log_blogger = logs("log_file3.txt", "INFO", "%(levelname)s %(asctime)s %(name)s %(message)s")

    def create_blog(self):
        try:
            self.log_blogger.log("Blog has been created", "INFO")
            msg = "Blog registered"
            self.log_blogger.log(f"{msg}", "INFO")
            return msg
        except Exception as e:
            self.log_blogger.log(e, "ERROR")

    


b= Blogs()
print(b.create_blog())

