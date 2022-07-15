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

class Affiliate_Institution:
    def __init__(self):
        self.logger_affiliate = logs('log_file2.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def Institute_check(self,Institute_name,Estd,Address):
        try:
            self.logger_affiliate.log("Institute Affiliate check", "INFO")
            update = [Institute_name,Estd,Address]
            message = "Institute details updated"
            self.logger_affiliate.log("FOllowing are the details for Institute Affiliation check","INFO")
            return message
        except Exception as e:
            self.logger_affiliate.log("Error occured","ERROR")

af = Affiliate_Institution()

print("Affiliation is ready ",af.Institute_check("Ineuron","2001","Bangalore"))