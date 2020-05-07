"""Generate sales report showing total melons each salesperson sold."""

# should put this in a function 
salespeople = []
melons_sold = []

#open text file
f = open('sales-report.txt') 

#iterate through each line in text 
for line in f:

    line = line.rstrip() # removes trailing white space

    entries = line.split('|') # splits line whereever there is a |
    

    salesperson = entries[0] #defines salepersons with their index (name)
    
   
    melons = int(entries[2]) #defines number of melons sold with their index
    
    #if salesperson is in list of salespeople
    if salesperson in salespeople:
    
        #define position as the index to access where to add melons sold in melons_sold
        position = salespeople.index(salesperson)
        melons_sold[position] += melons

    else:
         
        #adds salesperson if they arent on the list and num of melons they sold
        salespeople.append(salesperson)
        melons_sold.append(melons)


# for every sales person in salespeople, print how many melons they sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
