
#getting input
digi_time = input()

#finding length
length_digi = len(digi_time)

#using ord search to find out what is parenthesis and what isnt
for position in range(length_digi):

    #if the ord() of the position of digitime = ":", then thats how you find the rest
    if ord(digi_time[position]) == 58:
        first_parenthesis = position
        break
        
#using substrings to deternime what is what
hours = int(digi_time[0:first_parenthesis])
minutes = int(digi_time[first_parenthesis+1:first_parenthesis+3])
seconds = int(digi_time[first_parenthesis+4:length_digi])

#converting into seconds
hours_insec = hours*3600
minutes_insec = minutes*60

#priting
print(hours_insec+minutes_insec+seconds)