def print_produce_summary(day_number, day_deliveries):
    """ Given day number and day deliveries, produce report summary """


    print("Day:", day_number)
    the_file = open(day_deliveries) #opens file
    for line in the_file: # iterates through every line 
        line = line.rstrip()
        words = line.split('|')   #splits each line by the | and names it words

        #words = melon, count, amount

        melon = words[0] # word 0 is melons
        count = words[1] # word 1 is count
        amount = words[2] # word 2 is amount 

        print("Delivered {} {}s for total of ${}".format( 
            count, melon, amount))

    the_file.close() # closes file

print_produce_summary(1, "um-deliveries-20140519.txt")
print_produce_summary(2, "um-deliveries-20140520.txt")
print_produce_summary(3, "um-deliveries-20140521.txt")