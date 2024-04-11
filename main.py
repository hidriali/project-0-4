#this program is named CraFinder for a company named AutoCountry.
#the program enables users to navigate through the menu options.

def CarFinder():

  print("AutoCountry")

 #recall the fuction  
CarFinder()

# display the list of cars 

AllowedVehiclesList= [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']


#start your loop 
while True:
   print()
   print("*******************************")

   print("AutoCountry Vehicle Finder v0.1")
   print("*******************************")
# declare/assign your variables choice-num1, choice-num2, choice-num3.
   choice_num1=("1. PRINT all Authorized Vehicles") 

   choice_num2=("2. SEARCH for Authorized Vehicle")

   choice_num3=("3. add authorized vehicle")
  
   choice_num4=("4. DELETE Authorized Vehicle")
  
   choice_num5=("5. Exit")


#allow the user to enter a number from 1 to 4 of the menue. 
   user_input=input("Please Enter the  following number below from the following menu:"+ "\n" + choice_num1 + "\n" + choice_num2 + "\n" + choice_num3 + "\n" + choice_num4 + "\n"+ choice_num5 + "\n" )


  #declare the variable nameVehich and enable the user to input the name of the vehicle.
   if user_input=="1":
     #I used the *, "\n" to print element in new lines. 
      print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: " )
      print(*AllowedVehiclesList, sep = "\n")

# start your if statement to direct the user to the correct path after the user chooses a number from the menu.

#note must indent the codes below the while loop.


   if user_input == "4":
     nameVehich=input("Please Enter the full Vehicle name you would like to REMOVE:")
     # after the user enters the name of the vehicle, the program will append(one item) or add(one item) the name of the vehicle to the list.
     
     ask_user=input("Are you sure you want to remove "+" "+ (nameVehich) +" "+ "from the Authorized Vehicles List?" + "\n")
     if ask_user.lower()== "yes": 
      print("You have REMOVED " +""+ (nameVehich)+"as an authorized vehicle")
      AllowedVehiclesList.remove(nameVehich)
      if ask_user.lower()=="no":
        
        print()

#initilize continue statement to end the current iteration and start from the top of the program.

   continue