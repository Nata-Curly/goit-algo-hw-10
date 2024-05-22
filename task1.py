import pulp

model = pulp.LpProblem("Maximize total amount of produced beverages", pulp.LpMaximize)

A = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
B = pulp.LpVariable("FruitJuice", lowBound=0, cat="Integer")

model += A + B, "Total_beverages"

model += 2 * A + B <= 100, "Water"
model += A <= 50, "Sugar"
model += A <= 30, "LemonJuice"
model += 2 * B <= 40, "FruitPuree"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print("Maximum amount of Lemonade:", A.varValue)
print("Maximum amount of Fruit Juice:", B.varValue)
