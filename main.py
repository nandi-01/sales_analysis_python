import csv

occupations = {}
genders = {}
states = {}
products = {}

with open("diwali_sales.csv", "r") as csv_read:
    readers = csv.DictReader(csv_read)
    for reader in readers:
        occupation = reader["Occupation"] # Find out number of customers those work in Govt sector
        occupations[occupation] = occupations.get(occupation, 0) + 1

        gender = reader["Gender"]  # Find out number of genders are participated in sales
        genders[gender] = genders.get(gender, 0) + 1

        state = reader["State"]  # Find out number of states are participated in sales
        states[state] = states.get(state, 0) + 1

        product = reader["Product_ID"]  # Find out number of products sold per product id?
        products[product] = products.get(product, 0) + 1

print(occupations)
print(genders)
print(states)
print(products)
