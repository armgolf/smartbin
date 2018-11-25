#Import python packages

#Call initialisation script
#(initialisation script defines all variables).
sbintialisation.py

#conditions when Bin_state = 0
if Proximity_status_1 == 1: #if the door is opened go to binstate 1
    Bin_state = 1;

if Item_location_status != 0: #if there is still an item in upper compartments go to binstate 2
    Bin_state = 2;

#conditions when Bin_state = 1
if Timer_waiting >= 10: #nothing input for 10 seconds.
    Bin_state = 2;

#conditions when Bin_state = 2
if Proximity_status_1 == 1:
    Bin_state = 1;

if Item_location_status == 0:
    Bin_state = 0;
