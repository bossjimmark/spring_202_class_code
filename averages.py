# code intended to take the number entered by user
# and output sum, count, average

numbers=0
count=0
while True:
    num_entered=input("Enter as many numbers as desired. Enter q to quit: ")
    if num_entered=='q':
        break
    else:
        num_entered=int(num_entered)
        numbers+=num_entered
        count+=1

if count==0:
    print("You didn't enter anything.")   
else:
    print(f"The sum of the numbers entered is {numbers}")
    print(f"The count of the numbers entred is {count}")
    print(f"The average of the numbers entered is {numbers/count}")