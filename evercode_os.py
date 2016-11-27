# Import the os module.
import os

# Displays a message stating what is about to be done.
# Runs a system command within a try except environment.
# Either logs any errors that occurred or displays a completion message.
def run_command(task_message, command):
    
    print(task_message)
    
    try:
        return_value = os.system(command)
    
    except:
        print("Unknown error occured: %s" % sys.exc_info()[0])
        
    if return_value == 0:
        print("Completed successfully")
    else
        print("Completed with errors")