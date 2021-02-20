# code intended to take the number entered by user
# and output sum, count, average

numbers=0
count=0
while True:
    num_entered=input("Enter as many numbers as desired. Enter q to quit: ")
    try:
        num_entered=int(num_entered) # if user puts in q, error would be thrown here
        numbers+=num_entered
        count+=1
    except ValueError: # catches the error... 
        break

try:
    print(f"The sum of the numbers entered is {numbers}")
    print(f"The count of the numbers entred is {count}")
    print(f"The average of the numbers entered is {numbers/count}") # if no nums, error would occur
except ZeroDivisionError: # deal with div by zero error
    print("You didn't put in any numbers.")