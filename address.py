# file to gather address components from the user
# store the elements in a tuple 
# then print out the elements in a 4-line format

name=input("Enter your name as last name, first name: ")
address=input("Enter your street address: ")
other_address_info=input("Enter a PO Box if required: ")
city=input("Enter your city: ")
state=input("Enter your state: ") 
zip_code=input("Enter your zip code (first 5 digits only, please): ") 


last_name, first_name=name.split(",")          
address_number, address_street, address_street_type = address.split(" ")
address_street=address_street + " " + address_street_type 

user_address=last_name , first_name , address_number , address_street , other_address_info, city , state , zip_code

print(f"{user_address[0].title()},{user_address[1].title()}")
print(f"{user_address[2]} {user_address[3].title()}")
if other_address_info:
    print(f"{user_address[4].upper()}")
print(f"{user_address[5].title()} {user_address[6].upper()} {user_address[7]}")