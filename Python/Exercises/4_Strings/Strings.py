'''Create 3 variables to store street, city and country, now create address variable to store entire address.
 Use two ways of creating this variable, one using + operator and the other using f-string.
  Now Print the address in such a way that the street, city and country prints in a separate line'''
house_Number = '5-128'
street = 'Engineer Street'
place = 'Bethamcherla'
address = house_Number+", "+street+", "+place
print("Address:",address)
address = "{0},{1},{2}".format(house_Number,street,place)
print("Address using Formatted string",address)
address = f'{house_Number}\n{street}\n{place}'
print("Address using f-string:",address)

'''Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index'''
fact = "Earth revolves around the sun"
print(fact[6:15])
print(fact[-3:])
words_In_Fact = fact.split(" ")
print(words_In_Fact[1])
print(words_In_Fact[-1])

'''Create two variables to store how many fruits and vegetables you eat in a day. 
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables 
and fruits that you eat everyday. Use python f string for this.'''
fruits_I_Eat = ["Banana", "Pineapple", "Watermelon", "Apple", "Melon", "Papaya"]
vegetables_I_Eat = ["Carrot", "Beetroot", "Capcicum", "Radish", "Brinjal", "Littlefinger", "Tomato", "Onion"]
print("I eat {vegetables_Number} veggies and {fruits_Number} fruits daily".format(fruits_Number=len(fruits_I_Eat), vegetables_Number=len(vegetables_I_Eat)))


'''I have a string variable called s='maine 200 banana khaye'. 
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
Replace incorrect words in original strong with new ones and print the new string. 
Also try to do this in one line.'''
wrong_Statement = 'Maine 200 banana khaye'
correct_Statement = wrong_Statement.replace("banana", "samosa")
correct_Statement = correct_Statement.replace("200", "5")
#We can write two above statements in one line also
#correct_Statement = wrong_Statement.replace("banana", "samosa").replace("200","5")
print(correct_Statement)
