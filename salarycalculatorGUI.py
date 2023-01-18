"""
1/12/2023  Program: SalaryCalculatorGUI.py

Ivan's Python Final

A GUI-based Python project made from scratch. It's a simple Salary Calculator where your input is calculated based on your hourly wage and hours worked weekly. The output is also then calculated under the CALCULATE button giving you the correct output. The Colors used resemble the HULU Streaming app bc of it's green resembling money and sleek black background. 


NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# other imports can go here

class SalaryCalculatorGUI(EasyFrame):
	

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Hulu Calculator", background = "black")

		# widgets, rows and columns with input areas
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 3, sticky = "NSEW", font = Font(family = "Arial"), background = "green")
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0,  background = "darkseagreen")
		self.addLabel(text = "Number of Hours Worked:", row = 2, column = 0, background = "green")
		self.addButton(text = "Calculate", row = 3, column = 0, columnspan = 3, command = self.computeSlry)
		self.wage = self.addFloatField(value = 0.0, row = 1, column = 2, sticky = "NSEW")
		self.hours = self.addIntegerField(value = 0, row = 2, column = 2, sticky = "NSEW")
		

		# Salary Output
		self.addLabel(text = "Employee's Weekly Salary:", row = 4, column = 0, background = "darkseagreen")
		self.salary = self.addFloatField(value = 0.0, row = 4, column = 2)
		self.outputField = self.addFloatField(value = 0.0, row = 4, column = 2, precision = 2, state = "readonly")

	# defining the command function()
	def computeSlry(self):
		hourlyWage = self.wage.getNumber()
		hoursWorked = self.hours.getNumber()
		employeeSalary = hourlyWage * hoursWorked

		result = employeeSalary

		self.outputField.setNumber(result)



# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	SalaryCalculatorGUI().mainloop()

# global call to the main() method
main()


