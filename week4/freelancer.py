from employee import Employee
from job import Job

class Freelancer(Employee):
    def __init__(self, name, rate, job):
        super().__init__(name, rate)
        self.job = job

    @property
    def job(self):
        return self.__job
    
    @job.setter
    def job(self, new_job):
        self.__job = new_job

    # TODO: override salary
    @property
    def salary(self):
        return super().salary * self.job.man_month
    
    def __str__(self):
        return super().__str__() + f', working on {self.job}'
    
### Test ###
if __name__ == '__main__':
    mobile_app = Job('Mobile App', 4)
    john = Freelancer('John', 1.5, mobile_app)
    print(john)

    landing_page = Job('Landing Page', 0.5)
    paul = Freelancer('Paul', 1.0, landing_page)
    print(paul)
