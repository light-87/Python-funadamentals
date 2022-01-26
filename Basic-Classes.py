# Python Classes: Medical Insurance Project
# We have been asked to develop a system that makes it easier to organize patient data. WE will create a class that does the following:

# Takes in patient parameters regarding their personal information
# Contains methods that allow users to update their information
# Gives patients insight into their potential medical fees.



class Patient:
  # Building our Constructor
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
    # Adding Functionality with Methods
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(self.name + "'s estimated insurance cost is " + str(estimated_cost) + " dollars.")
  def update_age(self, new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.")
    # We also want to see what the new insurance expenses are
    self.estimated_insurance_cost()
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
  # Let’s update our method to accurately convey when we should use the noun “children” versus when we should use “child”.
    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    else:
      print(self.name + " has " + str(self.num_of_children) + "children.")
    self.estimated_insurance_cost()
    # Storing Patient Information
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information

# Let’s test out our __init__ method and create our first instance variable.
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)
# To test out the method
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
print(patient1.patient_profile())
