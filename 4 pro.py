class employee:
    def __init__(self, name, ID, department, job_tital):
        self.name=name
        self.ID=ID
        self.dept=department
        self.job=job_tital
    def set_department(self,department):
        self.__dept=department
    def set_job_tital(self,job_tital):
        self.__job=job_tital
    def get_name(self):
        return self.__name
    def get_ID(self):
        return self.__ID
    def get_department(self):
        return self.__dept
    def get_job_tital(self):
        return self.__job
    def __str__(self):
        return 'Name:' +self.__name+'\n'+\
            'ID number:'+str(self.__ID)+'\n'+\
            'Department:'+self.__dept+'\n'+\
            'Job tital:' +self.__job+'\n'
susan=employee('Susan Meyars', 2345, 'Accounting', 'voice prisedent')
mark=employee('Mark Jonis', 3434, 'dfsf', 'dwwwr')
print(susan)
print(mark)
