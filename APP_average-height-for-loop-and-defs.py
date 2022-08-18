student_heights = input("Input a list of student heights ").split()
for x in range(0, len(student_heights)):
  student_heights[x] = int(student_heights[x])

def added(list):
    total = 0
    for x in student_heights:
        total = total + x
    return total

🔎#   print(added(student_heights))

def counter(list):
    i = 0
    for x in student_heights:
        i += 1
    return i

🔎#   print(counter(student_heights))

median = (added(student_heights)) / (counter(student_heights))
print(round(median))



