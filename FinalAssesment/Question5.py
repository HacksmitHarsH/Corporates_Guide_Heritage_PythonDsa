#  number of employees
n = int(input())


highest_score = -1
best_employee_name = ""

#  Loop N times to read each employee record
for i in range(n):
    # Read the line  and split it into components
    record = input().split()
    
    emp_id = record[0]
    name = record[1]
    score = int(record[2]) 
    
    #  If we find a higher score, update our best employee tracker
    if score > highest_score:
        highest_score = score
        best_employee_name = name
        
    # \If the score is eqaul to the highest score we ve seen so far,
    # check if this employees name comes first alphabetically
    elif score == highest_score:
        if name < best_employee_name:
            best_employee_name = name


print(best_employee_name, highest_score)