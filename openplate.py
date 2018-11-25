
if Item_location[0] == Bin_compartment_1:
    Timer_plate = 0;
    start Timer_plate;
    Opening_plate_pwm_1 = 1;
    Opening_plate_pwm_1_completed = 0;
    if Timer_plate >= 1:
        Opening_plate_pwm_1_completed = 1;
        Timer_plate = 0;
        Opening_plate_pwm_1 = 0;

if Item_location[1] == Bin_compartment_2:
    Timer_plate = 0;
    start Timer_plate;
    Opening_plate_pwm_2 = 1;
    Opening_plate_pwm_2_completed = 0;
    if Timer_plate >= 1:
        Opening_plate_pwm_2_completed = 1;
        Timer_plate = 0;
        Opening_plate_pwm_2 = 0;

if Item_location[2] == Bin_compartment_2:
    Timer_plate = 0;
    start Timer_plate;
    Opening_plate_pwm_3 = 1;
    Opening_plate_pwm_3_completed = 0;
    if Timer_plate >= 1:
        Opening_plate_pwm_3_completed = 1;
        Timer_plate = 0;
        Opening_plate_pwm_3 = 0;

if Item_location[0] == Bin_compartment_1:
    Timer_plate = 0;
    start Timer_plate;
    Opening_plate_pwm_1 = 1;
    Opening_plate_pwm_1_completed = 0;
    if Timer_plate >= 1:
        Opening_plate_pwm_1_completed = 1;
        Timer_plate = 0;
        Opening_plate_pwm_1 = 0;
