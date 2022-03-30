from Database import mysql
from App import app


class Engineer:
    def __init__(self, degree, citizenship, gradeOnNPPE, enggWorkExperienceMonths):
        self.degree = degree
        self.citizenship = citizenship
        self.gradeOnNPPE = gradeOnNPPE
        self.enggWorkExperienceMonths = enggWorkExperienceMonths
