import sys

basic = int(sys.argv[1])
hra = 20/100 * basic
da = 10/100 * basic

gross_salary = basic + hra + da

print("gross salary :" , gross_salary)