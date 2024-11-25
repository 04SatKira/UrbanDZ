grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students ='Johnny','Bilbo','Steve','Khendrik','Aaron'
student_s=sorted(students)
s1=student_s[0]
s2=student_s[1]
s3=student_s[2]
s4=student_s[3]
s5=student_s[4]
a=(sum(grades[0])/len(grades[0]))
b=(sum(grades[1])/len(grades[1]))
c=(sum(grades[2])/len(grades[2]))
d=(sum(grades[3])/len(grades[3]))
e=(sum(grades[4])/len(grades[4]))
print({s1:a,s2:b, s3:c, s4:d, s5:e})