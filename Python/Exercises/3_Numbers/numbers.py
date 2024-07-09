'''You have a football field that is 92 meter long and 48.8 meter wide.
Find out total area using python and print it.'''

length = 92
breadth = 48.8
area = length*breadth
print("Area of football field",area)
print("Area of football field",round(area,2))

'''You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave 
shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?'''
packets_Bought = 9
packet_Cost = 1.49
money_Given = 20
returnable_Money = money_Given - (packets_Bought*packet_Cost)
print("Returnable money is ", returnable_Money)

'''You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
 If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
 Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)'''
side_Of_Tile = 5.5
area_Of_A_Tile = 5.5**2
print(area_Of_A_Tile)
cost_Per_Sqft = 500
total_Cost = area_Of_A_Tile*cost_Per_Sqft
print("Total cost to replace tiles ",total_Cost)

'''Print binary representation of number 17'''
#print("Binary representation of 17 is:", bin(17))
print("Binary representation of 17 is:", format(17, 'b'))
