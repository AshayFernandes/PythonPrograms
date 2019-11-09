
def OddRange(num1, num2):
  
  odd_array=[]
  for i in range(num1,num2):
     if (i%2!=0): 
        odd_array.append(i)
  return odd_array

    
num1=int(input("enter the lower number of the range")) 
num2=int(input("enter the highest number of the range"))
print_array=OddRange(num1,num2)
print("The array of odd numers between",num1," and ",num2,"is",print_array)

