#Q1

#Initialize variables
temperature = []
AvgT = 0
Name = ""
Year = 0
Month = 0
Day = 0 


#Input Monitored date and patient details
Year = int(input("Enter the Year :"))
Month = int(input("Enter the month :"))
Day = int(input("Enter the day :"))
Name =str(input("Enter the Patient Name :"))
print(Name,"'s temperature readings on :",Year,"-",Month,"-",Day,end ="")
print()
#Input 10 readings and find average temperature
for i in range(1,11):
   temperature.append(float(input(f"Enter temperature reading_{i} on celsius : ")))
AvgT =sum(temperature)/10
print(Name,"'s Average temperature for the day in celsius: % 0.1f"%AvgT)
fah = (AvgT*9/5)+32
print(Name,"'s Average temperature for the day in Fahreheit: % 0.1f"%fah)
#conditions to check Patient health status
if (fah >=97 and fah <=99) :
    print(Name,"'s body temperature is normal")
elif (fah>=99.1 and fah<=100.3) :
    print(Name,"'s have low grade fever")
elif (fah>=100.4) :
    print(Name,"'s have a fever caused by infection")
elif (fah<97) :
   print(Name,"'s have a hypothermia")
else :
   print("Check the temperature readings correctly and enter correct temperature value!")
