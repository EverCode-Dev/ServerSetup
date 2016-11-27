# Import the run_command function.
from evercode_os import run_command

# Import chdir from os to change the CWD.
from os import chdir

# Set the CWD to the EverCode Server Setup directory.
chdir("/root/evercode-setup")

# Synchronise with GitHub - useful for testing new scripts without a complete
# server wipe and reset.
run_command("Synchronising with GitHub...", "git pull")