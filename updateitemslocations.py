
if Rotate_blade_completed == 1:
    Item_location[0] = Item_location[3];
    Item_location[1] = Item_location[0];
    Item_location[2] = Item_location[1];
    Item_location[3] = Item_location[2];

if camera = 1:
    Item_location[1] = 6;

if response != 0:
    location = look for the last 6 in Item_location array;
    Item_location[location] = response;
    response = 0;

if Opening_plate_pwm_1_completed == 1:
    Item_location[0] = 0;
if Opening_plate_pwm_2_completed == 1:
    Item_location[1] = 0;
if Opening_plate_pwm_3_completed == 1:
    Item_location[2] = 0;
if Opening_plate_pwm_4_completed == 1:
    Item_location[3] = 0;
