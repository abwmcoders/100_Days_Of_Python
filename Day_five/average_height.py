print('Welcom to average height caculator')

student = input('Enter the students heights: ').split()
for n in range(0, len(student)):
    student[n] = int(student[n])
print(student)  
sum = 0
lenght = 0
for height in student:
    sum += height
    lenght +=1
print(lenght) 
print(sum)       

average_height = round(sum / lenght)
print (f"the average height is {average_height}")  
   
