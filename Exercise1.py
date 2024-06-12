from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

# Створюємо задачу лінійного програмування
model = LpProblem(name="maximize_beverage_production", sense=LpMaximize)

# Визначаємо змінні
L = LpVariable(name="Limonade", lowBound=0, cat='Continuous')
F = LpVariable(name="Fruit_Juice", lowBound=0, cat='Continuous')

# Додаємо цільову функцію
model += lpSum([L, F]), "Total Beverages"

# Обмеження
model += (2 * L + F <= 100, "Water Constraint")
model += (L <= 50, "Sugar Constraint")
model += (L <= 30, "Lemon Juice Constraint")
model += (2 * F <= 40, "Fruit Puree Constraint")

# Розвязання
status = model.solve()

# Виводимо результати
print(f"Статус: {model.status}, {LpStatus[model.status]}")
print(f"Оптимальна кількість лимонаду: {L.value()}")
print(f"Оптимальна кількість фруктового соку: {F.value()}")
print(f"Кількість напоїв узагальному: {L.value() + F.value()}")
