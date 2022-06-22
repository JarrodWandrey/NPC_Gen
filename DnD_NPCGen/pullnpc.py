import random

usedbin = []
def pull_npc():
    datastore = [] #empty list to store the read lines
    with open("npc.txt","r") as f:
        datastore = f.readlines() #read all lines in file
    if len(usedbin) == len(datastore): #checks if the usedbin is the same size as the total npcs loaded
        return("End of generated list, refresh")
    selected = random.choice(datastore) #selects a random value from the list
    while selected in usedbin:
        selected = random.choice(datastore) #selects a random value from the list
    usedbin.append(selected)#adds used selected character to usedbin to stop dups
    return(selected)