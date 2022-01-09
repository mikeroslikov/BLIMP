import RPi.GPIO as GPIO
import pigpio
import time
 
servo = 23
 
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)
 
pwm.set_PWM_frequency( servo, 50 )
 
pwm.set_servo_pulsewidth( servo, 2500 ) ;
time.sleep( 1 )
pwm.set_servo_pulsewidth( servo, 500 ) ;
time.sleep( 3 )

"""
print( "90 deg" )
pwm.set_servo_pulsewidth( servo, 1500 ) ;
time.sleep( 3 )
 
print( "180 deg" )
pwm.set_servo_pulsewidth( servo, 2500 ) ;
time.sleep( 3 )

"""
# turning off servo
pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_frequency( servo, 0 )