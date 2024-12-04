grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average1=sum(grades[0][0:])/len(grades[0])
average2=sum(grades[1][0:])/len(grades[1])
average3=sum(grades[2][0:])/len(grades[2])
average4=sum(grades[3][0:])/len(grades[3])
average5=sum(grades[4][0:])/len(grades[4])
average=average1,average2,average3,average4,average5
list(average)
set_students= {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
set_students= list(set_students)
set_students.sort()
dictionary = dict (zip(set_students,average))
print(dictionary)