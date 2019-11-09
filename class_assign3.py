def HourMinute(num):
  hour=int(num/60)
  minute=(num%60)
  date=[hour,":",minute]
  final_format="" 
  for x in date:
    final_format+=str(x) 
  return final_format

result=HourMinute(int(input("enter the number of mintues")))
print(result)
