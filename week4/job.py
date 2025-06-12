class Job:
    def __init__(self, name, man_month):
        self.name = name
        self.man_month = man_month

    # TODO: getter/setter for name
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Error: Name cannot be empty')
        
        self.__name = new_name

    @property
    def man_month(self):
        return self.__man_month
    
    @man_month.setter
    def man_month(self, new_mm):
        if new_mm <= 0:
            raise ValueError('Error: Man month must greater than 0')
        
        self.__man_month = new_mm

    def __str__(self):
        return f'Job: {self.name}, total {self.man_month} man months'
    
#### Test ####
if __name__ == '__main__':
    mobile_app = Job('Mobile App', 4)
    print(mobile_app)

    landing_page = Job('Landing Page', 0.5)
    print(landing_page)