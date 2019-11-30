from datetime import date

def AgeConvert(num):
   month_days=0
   actual_days=0
   days=0
   age=[]
   split_date=num.split('-')
   today = date.today()
   today_date=str(today)
   split_today_date=today_date.split('-')
   for i in range(0,len(split_today_date)):
       age.append(int(split_today_date[i])-int(split_date[i]))
   days=age[0]*365
   if(age[1]<0 or age[2]<0):
     if(age[1]<0):
       month_days=abs(age[1])*30
     if(age[2]<0):
       actual_days=abs(age[2])
    
   total_days=days-month_days-actual_days      

   return total_days
        
    
DOB=input("enter your birth date in the format year-month-day")

age_limit=AgeConvert(DOB)
years=int(age_limit/365)
days=(age_limit%365)
print("you are ",years," years",days," days old")
