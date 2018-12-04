#Import python packages/files
import sbinitialisation; #initialisation script defines all variables.
#read proximity sensor 1 (door open/closed).
import proximitysensor1;

#conditions when bin_state = 0
#if the door is opened go to binstate 1
if proximitysensor1.object == True:
    bin_state = 1;

#if there is still an item in upper compartments go to binstate 2
if sbinitialisation.item_location_status != 0:
    bin_state = 2;

#conditions when bin_state = 1
#nothing input for 10 seconds.
if timer_waiting >= 10:
    bin_state = 2;

#conditions when bin_state = 2
#if the door is opened go to bin_state 1
if sbinitialisation.proximity_status_1 == 1:
    bin_state = 1;

#if there are no items in the upper compartments go to bin_state0
if sbinitialisation.item_location_status == 0:
    bin_state = 0;

#Call functionality based on bin_state.
if bin_state == 0:
    import binstatus0;

if bin_state == 1:
    import binstatus1;

if bin_state == 2:
    import binstatus2;
