import logging

class logs:
    def __init__(self, filename, level, format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename, level=self.level, format=self.format)


    def log(self,message, method):
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)


class COurses:
    def __init__(self, course_Id, sub_course):
        self.course_Id = course_Id
        self.sub_course = sub_course
        self.log_courses = logs("log_file4.txt","INFO", "%(levelname)s %(asctime)s %(message)s")

    def new_course(self):
        try:
            self.log_courses.log("log for registring new course", "INFO")
            result ="New course created"
            return result
        except  Exception as e:
            self.log_courses.log("registration failed" , "ERROR")

class no_of_courses:
    def __init__(self):
        self.course_count = 30
        self.log_courses = logs("log_file4.txt","INFO", "%(levelname)s %(asctime)s %(message)s")

    def count_course(self):
        try:
            msg = f"Total registered courses at INeuron", {self.course_count}
            self.log_courses.log(msg, "INFO")
            return msg
        except Exception as e:
            self.log_courses.log(e, "ERROR")


class job:
    def __init__(self):
        self.log_courses = logs("log_file4.txt", "INFO", "%(levelname)s %(asctime)s %(message)s")
    def Jobs_type(self, job_type):
        try:
            self.log_courses.log("Job search on the basis of job type", "INFO")
            if job_type == 'Part time':
                result = "Go for either Permanent Job or Freelancing"
            elif job_type == 'Full time':
                result  = "Thats a good choice"
            else:
                result = "On Bench"
            self.log_courses.log("These can be choices to opt for a job type", "INFO")
            return result
        except Exception as e:
            self.log_courses.log(e, "ERROR")


class Intenship:
    def __init__(self):
        self.log_courses = logs("log_file4.txt", "INFO", "%(levelname)s %(asctime)s %(message)s")
    def internship_avialability(self,intern):
        try:
            self.log_courses.log("Internship program need to be checked", "INFO")
            if intern == "Machine Learning":
                opt = "Opt for ML"
            elif intern == "Data science":
                opt = " opt for DS"
            else:
                opt  = "opt for Data analytics"
            self.log_courses.log("opt for either internship programs","INFO")
            return opt
        except Exception as e:
            self.log_courses.log(e,"ERROR")

class ContactUs:
    def __init__(self):
        self.log_courses = logs("log_file4.txt", "INFO", "%(levelname)s %(asctime)s %(message)s")

    def contact_details(self):
        try:
            msgs = "mail us at support@ineuron.ai"
            self.log_courses.log(msgs, "INFO")
            return msgs
        except Exception as e:
            self.log_courses.log(e, "ERROR")

c = ContactUs()
print("In case you need help please reach out to us using ", c.contact_details())


int  = Intenship()
print("Any of the internship programs are selected", int.internship_avialability("Data science"))





jt = job()
print("Suggested jobs are ", jt.Jobs_type("Part time"))



cr= COurses("Data Science", "Data analytics")
print(cr.new_course())

nc= no_of_courses()
print(nc.course_count)





