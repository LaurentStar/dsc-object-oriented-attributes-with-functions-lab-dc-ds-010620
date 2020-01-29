class School:
	def __init__(self, name):
		self.name = name
		self.roster = {}
		
	def add_student(self, name, grade_level):
		if grade_level not in self.roster.keys():
			self.roster[grade_level] = []
		
		if name not in self.roster[grade_level]:
			self.roster[grade_level].append(name)
			
	def grade(self, grade_level):
		return self.roster[grade_level]
	
	def sort_roster(self):
		for _ in self.roster.keys():
			self.roster[_].sort()
		return self.roster
