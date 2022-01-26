# Suppose we are a medical professional curious about how certain factors contribute to medical insurance costs. Using a formula that estimates a person’s yearly insurance costs, we will investigate how different factors such as age, sex, BMI, etc. affect the prediction.


# created the initial variables below for a 28-year-old, nonsmoking woman who has three children and a BMI of 26.2.
age = 28
smoker = 0
sex = 0
bmi = 26.2
num_of_children = 3

# Added insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")
# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")
# Male vs. Female Factor
sex = 1
bmi = 26.2
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars")

# In this way different factors affect the Medical Insurance