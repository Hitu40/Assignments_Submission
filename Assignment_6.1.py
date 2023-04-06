import json

class Employee:
    def _init_(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def _str_(self):
        return f"{self.name} ({self.dob}) - {self.height}cm - {self.city}, {self.state}"

# Read the JSON file
with open("employee.json", "r") as f:
    data = json.load(f)

# Extract the employee information from the JSON data and create Employee objects
employees = []
for emp_data in data["employees"]:
    name = emp_data["name"]
    dob = emp_data["dob"]
    height = emp_data["height"]
    city = emp_data["city"]
    state = emp_data["state"]
    emp = Employee(name, dob, height, city, state)
    employees.append(emp)

# Print the list of Employee objects
for emp in employees:
    print(emp)