salary = int(input("Salary? "))
grade = input("Grade? ")
dept = input("Dept? ")

if salary > 15000:
    if dept == 'IT':
        if int(grade) < 11:
            tax = 9
        if int(grade) > 10:
            tax = 17
        if grade == 'CTO':
            tax = 2
    if dept == 'HR':
        if int(grade) < 11:
            tax = 9
        if int(grade) > 10:
            tax = 15
        if grade == 'CTO':
            tax = 0
tax = 0

if dept not in ('IT', 'HR'):
    print("Invalid Dept")
    exit()

if dept == 'IT':
    bonus = 5
if dept == 'HR':
    bonus = 0

salary = salary + (salary / 100 * int(bonus))
gross = salary - (salary / 100 * int(tax))

print("Gross: %s" % gross)
