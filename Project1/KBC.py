import time

# python and dsa questions list
questions = [
    {"q": "What is the correct file extension for Python files?", 
     "op": ["A. .pt", "B. .pyt", "C. .py", "D. .txt"], 
     "ans": "C"},
    
    {"q": "Which data structure follows the LIFO (Last In, First Out) principle?", 
     "op": ["A. Queue", "B. Array", "C. Linked List", "D. Stack"], 
     "ans": "D"},
    
    {"q": "Which keyword is used to define a function in Python?", 
     "op": ["A. def", "B. func", "C. define", "D. function"], 
     "ans": "A"},
    
    {"q": "What is the time complexity of accessing an element in an array by its index?", 
     "op": ["A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n^2)"], 
     "ans": "A"},
    
    {"q": "Which of these data types is mutable in Python?", 
     "op": ["A. Tuple", "B. String", "C. List", "D. Integer"], 
     "ans": "C"},
    
    {"q": "Which data structure follows the FIFO (First In, First Out) principle?", 
     "op": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"], 
     "ans": "B"},
    
    {"q": "What does the '//' operator do in Python?", 
     "op": ["A. Exponentiation", "B. Floor Division", "C. Modulus", "D. Commenting"], 
     "ans": "B"},
    
    {"q": "Which sorting algorithm is known to have a worst-case time complexity of O(n^2)?", 
     "op": ["A. Merge Sort", "B. Heap Sort", "C. Bubble Sort", "D. Radix Sort"], 
     "ans": "C"},
    
    {"q": "How do you add an element to the end of a list in Python?", 
     "op": ["A. list.add()", "B. list.insert()", "C. list.push()", "D. list.append()"], 
     "ans": "D"},
    
    {"q": "Which data structure is best suited for representing hierarchical relationships?", 
     "op": ["A. Array", "B. Stack", "C. Tree", "D. Queue"], 
     "ans": "C"},
    
    {"q": "What is the average time complexity of searching for a key in a Python dictionary?", 
     "op": ["A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n log n)"], 
     "ans": "A"},
    
    {"q": "Which of the following is NOT a built-in data structure in Python?", 
     "op": ["A. Dictionary", "B. Tuple", "C. Set", "D. Linked List"], 
     "ans": "D"}
]

prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
print("               ")
print("Welcome to KBC")
print("_______________")

level = 0
money_won = 0
used_50 = False
used_skip = False

# main game loop
while level < 10:
    current_q = questions[level]
    prize_money = prizes[level]
    
    print("\nQuestion", level + 1, "for Rs.", prize_money)
    print(current_q["q"])
    
    # print options one by one
    print(current_q["op"][0])
    print(current_q["op"][1])
    print(current_q["op"][2])
    print(current_q["op"][3])
    
    start_time = time.time()
    ans = input("Enter A, B, C, D or 50 or SKIP: ").upper()
    end_time = time.time()
    
    # check time
    if end_time - start_time > 30:
        print("Time is up!")
        break

    # 50-50 lifeline
    if ans == "50":
        if used_50 == False:
            used_50 = True
            print("50-50 Lifeline used! Two options left:")
            
            # beginner hack to just print the correct answer and one random other answer
            for o in current_q["op"]:
                if current_q["ans"] in o:
                    print(o)
            if current_q["ans"] == "A":
                print(current_q["op"][1]) # print B if A is correct
            else:
                print(current_q["op"][0]) # print A if something else is correct
                
            ans = input("Enter answer again: ").upper()
        else:
            print("You already used 50-50!")
            ans = input("Enter answer again: ").upper()

    # skip lifeline
    if ans == "SKIP":
        if used_skip == False:
            used_skip = True
            print("Question skipped!")
            # just move to the next question in the list and pretend it was the same level
            level = level + 1
            current_q = questions[level]
            print(current_q["q"])
            print(current_q["op"][0])
            print(current_q["op"][1])
            print(current_q["op"][2])
            print(current_q["op"][3])
            ans = input("Enter answer: ").upper()
        else:
            print("You already used skip!")
            ans = input("Enter answer again: ").upper()

    # check if answer is right
    if ans == current_q["ans"]:
        print("Correct Answer!")
        money_won = prize_money
        level = level + 1
    else:
        print("Wrong Answer! The correct answer was", current_q["ans"])
        break

print("\nGAME OVER")
print("Total money won: Rs.", money_won)