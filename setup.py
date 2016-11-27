# Import the run_command function.
from evercode_os import run_command

# Import chdir from os to change the CWD.
from os import chdir

# Move the CWD into the EverCode Setup directory.
chdir("/root/evercode-setup")

# Store the setup version number.
setup_version_number = "1.0.1"

# Save the version number to root.
run_command("Saving version number...", "echo 'EverCode Server from version %s' > /evercode.version" % setup_version_number)

# Set execute rights on shell scripts.
run_command("Setting execute rights on shell scripts...", "chmod u+x *.sh")

# Add a symlink to "/var/www/html".
run_command("Adding symlink to public web folder...", "ln -s /var/www/html /root/html")