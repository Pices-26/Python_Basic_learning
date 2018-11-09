employee_files = open('employees.txt', 'r')

print(employee_files.readable())
print(employee_files.read())
'''running the command below again will print out the next line'''
print(employee_files.readline())


print(employee_files.readlines()[1])


for employee in employee_files.readlines():
    print(employee)


employee_files.close()

