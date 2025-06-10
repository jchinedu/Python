# trying object and classes in python 
class student:
	def __init__(self, name, major, gpa, is_on_probation):
		self.name = name
		self.major = major	
		self.gpa = gpa
		self.is_on_probation = is_on_probation
	def __on_honor_role(self):
		if self.gpa >= 3.5:
			return True
		else:
			return False
	def __repr__(self):
       		return (f"student(name={self.name!r}, major={self.major!r}, "
                f"gpa={self.gpa}, is_on_probation={self.is_on_probation})")