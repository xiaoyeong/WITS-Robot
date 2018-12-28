import datetime as dt
from time import sleep

#from displayLED import *
from mediaAPI import *
from scheduleAPI import *
from webcam_gui import *
    
    
def main():
	schedule = read_schedule('./data/schedule')
	
	hourly_alert = 1  # alerts once for a certain hour
	activity_alert = 1  # alerts once for a certain activity
    
	while True:
		current_time = dt.datetime.now().strftime("%H:%M")
		print_to_screen("Current Time: " + current_time)
        
		if timing_exists(current_time, schedule):
			"""
			If there is an activity, the robot will be blocked until the activity is finished.
			"""
			
			if activity_alert:
				activity_alert = 0
				print_timing_activity(current_time, schedule[current_time])
				#displayLED(0)
				play_audio('./sounds/activity.wav')
				# TODO: Add in physical action
				initialize_webcam_gui()
				# TODO: Add in noise and action if activity is not completed.
				
                
		else:
			"""
			If there is no activity, the robot acts like a clock with hourly actions.
			"""
			
			activity_alert = 1
			
			if current_time[3:5] == '00':  # if it is a full hour timing
				if hourly_alert:
					hourly_alert = 0
					#displayLED(3)
					play_audio('./sounds/hourly.wav')
					# TODO: Add in physical action
			else:
				hourly_alert = 1
				#displayLED(2)
				#play_audio('./sounds/angry.wav')
				
			sleep(1)
			clear_screen_text("Current Time: " + current_time)

        
if __name__ == "__main__":
	main()
