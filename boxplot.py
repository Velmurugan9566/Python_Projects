
#Read the data from a CSV file
data = open('student_marks.csv','r')
print(data.read())
'''# Create a boxplot to visualize the data
plt.figure(figsize=(8, 6))
plt.boxplot([data['Python'],data['Maths'],data['Dataengineering'],data['Java'],data['SoftComputing']],labels=['Python','Maths','DataEngineering','Java','SoftComputing'], vert=1)
plt.title('Student Performance in Annual Examination')

plt.show()
name=['Python','Maths','Dataengineering','Java','SoftComputing']

#Detect and identify outliers
for i in name:
    Q1 = data[i].quantile(0.25)
    Q3 = data[i].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[i] < lower_bound) | (data[i] > upper_bound)]
    if not outliers.empty:
        print(i," Outliers:")
        li=outliers.astype(str)
        print('Student Name: ',li['Stuname'],'\nMark :',li[i],'\n')
    else:
        print(i,' :no outliers\n')'''
