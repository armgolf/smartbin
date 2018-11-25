
#Internal variables:
Item_location_1 = 0; #item in Item_location array in the first top compartment
Item_location_2 = 0; #item in Item_location array in the second  top compartment
Item_location_3 = 0; #item in Item_location array in the third top compartment
Item_location_4 = 0; #item in Item_location array in the fourth top compartment
Item_location = [Item_location_1, Item_location_2, Item_location_3, Item_location_4]; #array of top compartments (zero is empty, 1, 2, 3, 4 is material types, 5 is not pictured yet and unidentified material, 6 is pictured but not yet identified)

Item_location_status = 0; #Sum of items present in 4 compartments. 0 to 4

Bin_state = 0; #0, 1, 2 for the status of the Bin (0 = standby, 1 = waiting for new item, 2 = emptying compartments)
Timer_waiting = 0; #Timer waiting for item to be placed in the bin
Timer_plate = 0; #how long to open and close the plates
Timer_blade = 0; #how long to rotate the top blade for

Opening_plate_pwm_1_completed = 0; #opening plate in location 1 has completed
Opening_plate_pwm_2_completed = 0;
Opening_plate_pwm_3_completed = 0;
Opening_plate_pwm_4_completed = 0;

Output variables:
Opening_plate_pwm_1 = 0; #Opening plates in location 1
Opening_plate_pwm_2 = 0;
Opening_plate_pwm_3 = 0;
Opening_plate_pwm_4 = 0;

Rotate_blade_pwm = 0; #rotate top blade 90 degrees
Rotate_blade_completed = 0; #blade has rotated 90 degrees

Input variables:
Bin_compartment_1 = 1; #Bin bottom compartment 1 contents (1 to 4)
Bin_compartment_2 = 2; #Bin bottom compartment 1 contents (1 to 4)
Bin_compartment_3 = 3; #Bin bottom compartment 1 contents (1 to 4)
Bin_compartment_4 = 4; #Bin bottom compartment 1 contents (1 to 4)

Camera_detection = 0; #Object type from NN

Proximity_status_1 = 0; #0 or 1 for the bin door
Proximity_status_2 = 0; #0 or 1 for the item present in the compartment

#Check for present items and update variables
#Rotate 4 times and update Item_location array.
