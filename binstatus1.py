#The door is open, read proximity sensor 2 (identify if object is present in compartment or not)
import proximitysensor2
#timer is a function of threading
import threading

#nothing in the top compartment
if Item_location[0] == 0 and proximitysensor2.object == False:
    t = Timer(30.0, waited = True)
    t.start() # after 30 seconds, waited is assigned to True

#unknown item present
if Item_location[0] == 0 and proximitysensor2.object == True:
    Item_location[0] = 5
    #rotate 90 degrees
    #import rotate #rotate objects in the top compartment 90 degrees
    #import updateitemlocations #reassign compartment contents after rotation
    import photo #capture image of the object and assign it to variable
    import nanoclass1 #identify object in the image captured
    #import updateitemlocations #reassign compartment contents after object identification

#Check if items are in the correct location to be emptied and empty
if Item_location[0] == Bin_compartment_1 or Item_location[1] == Bin_compartment_2 or Item_location_[2] == Bin_compartment_3 or Item_location_[3] == Bin_compartment_4:
    import openplate

import binstatus2
