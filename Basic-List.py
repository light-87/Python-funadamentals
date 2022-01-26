# Working with Python Lists: Medical Insurance Costs Project
# we are a doctor sorting through medical insurance cost data for some patients.

# Using our knowledge of Python lists, we will store medical data and see what valuable insights you can gain from that data.


names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Appending Data
names.append("Priscilla")
insurance_costs.append(8320.0)
# Combining Names and insurance Data
medical_records = list(zip(insurance_costs, names))
print(medical_records)
# Storing len of records
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")
# Selecting first record
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))
# Sorting the records
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))
# Cheapect 3 records
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))
# Priciest 3 records
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))
# Counting Elements in a list
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")