import random
import re

# By omthegg on github

tehran_c = ['001', '002', '003', '004', '005', '006', '007', '008', '011'
            , '020', '025', '015', '043']
# Fun fact: Robat karim's code is 666

def has_valid_3_digits(code:str):
    first_3 = str(str(code[0])+str(code[1])+str(code[2]))
    return first_3 in tehran_c

def is_valid_iran_code(code):
    if not re.search(r'^\d{10}$', code): return False
    check = int(code[9])
    s = sum(int(code[x]) * (10 - x) for x in range(9)) % 11
    return check == s if s < 2 else check + s == 11

c_file = open("CodeList.txt", "a+")
p_file = open("CodePasswordList.txt", "a+")

c_list = []
p_list = []

c_list = c_file.read().split("\n")
p_list = c_file.read().split("\n")

if c_list[0] == "\n":
    del c_list[0]

if p_list[0] == "\n":
    del p_list[0]

times = int(input("How many? "))


y = ['y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'YeS', 'yES', 'yEs', 'yeS']
n = ['n', 'N', 'no', 'No', 'nO']
global tehran
global t
t = str(input("Only generate Tehran codes?(y / n) "))

while not(t in y) and not(t in n):
    t = str(input("Only generate Tehran codes?(y / n) "))

tehran = t in y

global i
i = 0
while i < times:
    c = "0"
    p = ""
    
    for j in range(9):
        c = str(c+str(random.randint(0, 10)))
    
    e = 0
    for j in range(len(c)):
        if j > 9:
            e += 1
    
    c = c[0:len(c)-e]

    if is_valid_iran_code(c) and not (c in c_list):
        if tehran:
            if has_valid_3_digits(c):
                print(c)
                p = str(str(c[6])+str(c[7])+str(c[8])+str(c[9]))
                print(p)
        
                c_list.append(c)
                p_list.append(p)

                i += 1
        else:
            print(c)
            p = str(str(c[6])+str(c[7])+str(c[8])+str(c[9]))
            print(p)

            c_list.append(c)
            p_list.append(p)

            i += 1

        
print("Finished generating.")

print("Writing to code file...")

for i in c_list:
    c_file.write(str(i+"\n"))

c_file.close()

print("Writing to password file...")
for i in p_list:
    p_file.write(str(i+"\n"))

p_file.close()

print("Finished writing.")
print("Press Enter to exit.")

input()
