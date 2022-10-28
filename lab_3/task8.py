money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
s = 0
month = 0  # количество месяцев, которое можно прожить
money = 1
sum_capital = 1
sum_spend = 0

while money > sum_spend:
    sum_capital = money_capital + salary
    sum_spend = spend + s
    money = sum_capital - sum_spend
    money_capital = money
    month += 1
    s = spend * 0.05 * month
print(month)
