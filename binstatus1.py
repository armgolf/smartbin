#The door is open, read proximity sensor 2 (identify if object is present in compartment or not)
import proximitysensor2;

#nothing in the top compartment
if Item_location[0] == 0 and proximitysensor2.object == False:
    Timer_waiting = 0;
    start Timer_waiting

#unknown item present
if Item_location[0] == 0 and proximitysensor2.object == True:
    Item_location[0] = 5;
    #rotate 90 degrees
    import rotate
    import updateitemlocations
    import photo
    nanoclass1.py 001.jpg #identification script with images as argument
    updateitemlocations.py

#Check if items are in the correct location to be emptied and empty
if Item_location[0] == Bin_compartment_1 or Item_location[1] == Bin_compartment_2 or Item_location_[2] == Bin_compartment_3 or Item_location_[3] == Bin_compartment_4:
    openplate.py

binstatus2.py
