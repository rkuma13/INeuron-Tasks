import logging

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



class Ineuron:
    def __init__(self,student_name, Class_type, courses_registered, DOB):
        self.student_name = student_name
        self.Class_type = Class_type
        self.courses_registered = courses_registered
        self.DOB = DOB

        self.logger = logs("log_inherit.txt", "INFO", "%(levelname)s %(asctime)s %(name)s %(message)s")

        self.logger.log("Construtors created","INFO")

    def age(self, Current_year):
        try:
            self.logger.log("age will be calculated", "INFO")
            calculate = Current_year - self.DOB
            return calculate
            self.logger.log(f"{self.student_name} is the Age of the student", "INFO")

        except Exception as e:
            self.logger.log(e, "ERROR")

student1 = Ineuron("Rajan", "Full time", "FSDS", 1993)
print(student1.age(2022))


class Ineuron_Students(Ineuron):
    logging.info("inheriting the proporties from parent class")
    try:
        def classe(self, name, faculty):
            self.logger.log("constructor for the classe", "INFO")
            if faculty == "Sudhanshu sir":
                return "Lecture on Python"
            elif faculty == "Krish Naik":
                return "Lecture on Stats"
            elif faculty == "Naveen Sir":
                return "Lecture on Java"
            else:
                return "no classes"
    except Exception as e:
        self.logger.log(e, "ERROR")

student2 = Ineuron_Students("Rajan Kumar","Full time", "Maths", 1991)
print(student2.classe("Rajan Kumar","Sudhanshu sir"))

class Jobs():
    def job_search(self):
        msg = "YOu are eligible for job"
        return msg

class Details(Ineuron_Students,Jobs):
    logging.info(("inheriting Student class and Ineuron Class"))

    def details1(self):
        try:
            self.logger.log("Detail of the student at Ineuron", "INFO")
            return self.student_name, self.courses_registered, self.Class_type, self.DOB
        except Exception as e:
            self.logger.log(e, "ERROR")

student3 = Details("Rohit", "Part time","BOOTcamp", 1995)
print(student3.details1())
print(student3.age(2023))
print(student3.classe("Rohit","Krish Naik"))
print(student3.job_search())






