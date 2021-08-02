# [] | creates a list
emp_lst = ["akash", "vijay", "vinay", "akash"]
for emp in emp_lst:
    print(emp.upper())

print("---------------")
# {} | creates a set
# set function can be used to create a set from iterable

emp_set = set(emp_lst)
for emp in emp_set:
    print(emp)

print("---------------")

for name in {'test', 'test', 'test'}:
    print(name)
