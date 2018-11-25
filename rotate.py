
start Timer_blade timer
Rotate_blade_pwm == 1;
Rotate_blade_completed == 0;

#blade rotates 90 degrees
if Timer_blade >= 1:
     Rotate_blade_pwm == 0;
     Timer_blade = 0;
     Rotate_blade_completed = 1;
