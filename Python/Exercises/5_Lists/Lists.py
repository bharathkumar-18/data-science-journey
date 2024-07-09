'''Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out'''
'''1. In Feb, how many dollars you spent extra compare to January?'''
expenses = [2200, 2350, 2600, 2130, 2190]
print(expenses[1]-expenses[0])
'''2. Find out your total expense in first quarter (first three months) of the year.'''
quarter_Expenses = 0
for i in range(0,3):
    quarter_Expenses = quarter_Expenses + expenses[i]
print(quarter_Expenses)
'''3. Find out if you spent exactly 2000 dollars in any month'''
if 2000 in expenses:
    print("Yes")
else:
    print("No")
'''June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list'''
expenses.append(1980)
print(expenses)
'''You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''
expenses[3] = expenses[3] - 200
print(expenses)


'''You have a list of your favourite marvel super heros.'''
heros=['spider man','thor','hulk','iron man','captain america']
'''Using this find out,'''

'''1. Length of the list'''
print("Length of heros",len(heros))
'''2. Add 'black panther' at the end of this list'''
heros.append('black panther')
print("After adding black panther ", heros )
'''3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk' '''
heros.remove('black panther')
heros.insert(3, 'black panther')
print("After adding black panther before hulk ", heros)
'''4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.'''
heros[1:3] = ['doctor strange']
'''5. Sort the heros list in alphabetical order 
(Hint. Use dir() functions to list down all functions available in list)
'''
print(dir(heros)) #Gives all of the things that can be done
heros.sort()
print("Printing in ascending order:", heros)
heros.sort(reverse=True)
print("Printing in descending order: ", heros)
heros.sort(key=len)
print("Printing in ascending order based on length of each element:", heros)
