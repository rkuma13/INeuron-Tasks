import logging

##logging.basicConfig(filename="ClassesTasks.log", level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')


class logs:
    def __init__(self, filename, level, format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename, level=self.level, format=self.format)

    def log(self, message, method):
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)


class Ineuron_students:
    def __init__(self, name, classes, course):
        self.name = name
        self.classes = classes
        self.course = course
        self.logger = logs("log_file.txt", "INFO", "%(levelname)s %(asctime)s %(name)s %(message)s")

    def new_admission(self):
        try:
            self.logger.log(f"{self.name} are new admission in Ineuron under course {self.course}", "INFO")
            return f"Welcome in INeuron {self.name} under {self.course} course and timing will be {self.classes}"
        except Exception as e:
            self.logger.log(e,"ERROR")


i= Ineuron_students("Rajan", "Evening Classes", "FSDS BOOTCamp")
print(i.new_admission())

