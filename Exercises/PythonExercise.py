carCompany = ('BMW', 'Ford', 'Mercedes', 'Audi', 'Toyota', 'Kia')

print(carCompany[1])

print(carCompany[1:5])

carComp = list(carCompany)

carComp.remove('Kia')

print(carComp)

carComp.append('Tesla')

print(carComp)

carComp.append('Kia')

print(carComp)

carComp.remove('Audi')

print(carComp)

carCompany = tuple(carComp)

print(carCompany)

carDict = {
    "Car Company": "tesla",
    "Color": "white",
    "Model": "3",
    "Model_year": "2020"
}

x = carDict["Color"]
y = carDict["Model"]
z = carDict["Model_year"]

print(x)
print(y)
print(z)

carDict["Color"] = "red"
print(carDict["Color"])

carDict["Type"] = "sedan"

print(carDict)