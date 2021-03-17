#Python- Calculation of standard deviation in Python
#Computer Programming Tutor_YT_16 March 2021

Data = [11,25,14,12,13,67,44]
sum =0
for i in range(len(Data)):
    sum+= Data[i]
mean_of_datas = sum/len(Data)

sum_of_squared_deviation = 0
for i in range(len(Data)):
    sum_of_squared_deviation+= (Data[i] - mean_of_datas )**2
Standard_Deviation = ((sum_of_squared_deviation)/len(Data))**0.5
print("Standard Deviation of Sample is:","%.4f"%(Standard_Deviation))








#"%.2f"%
