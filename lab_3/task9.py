salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
spend_increase = 0

i = 0  # количество денег, чтобы прожить 10 месяцев

sum_salary = salary * months
for i in range(10):
        spend_increase = spend_increase + spend + spend * increase * i
        i += 1
int(spend_increase)
print(int(spend_increase)-sum_salary)

