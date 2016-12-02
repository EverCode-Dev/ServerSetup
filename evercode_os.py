# Import the os module for running commands.
import os

# Import the datetime module for building timestamps.
import datetime

# Print a message to the console prepending a timestamp.
def print_message(message):
    
    # Build the timestamp.
    timestamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
    
    # Log the message.
    print("%s: %s" % (timestamp, message))

# Displays a message stating what is about to be done.
# Runs a system command within a try except environment.
# Either logs any errors that occurred or displays a completion message.
def run_command(task_message, command, optional_follow_up_command = ""):
    
    print_message(task_message)
    
    try:
        return_value = os.system(command)
    
    except:
        print_message("Unknown error occured: %s" % sys.exc_info()[0])
        
    if return_value == 0:
        if optional_follow_up_command != "":
            os.system(optional_follow_up_command)
        else:
            print_message("Completed successfully.")
        print()
    else:
        print_message("Completed with errors.")