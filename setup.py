# Import the run_command function.
from evercode_os import run_command

# Import chdir from os to change the CWD.
from os import chdir

# Import the sys module to get arguments.
import sys

# Move the CWD into the EverCode Setup directory.
chdir("/root/evercode-setup")

# Store the setup version number.
setup_version_number = sys.argv[1]

# Start the setup.
print("Running EverCode Server Setup version %s" % setup_version_number)

# Save the version number to root.
run_command("Saving version number...", "echo 'EverCode Server from version %s' > /evercode.version" % setup_version_number)

# Set execute rights on shell scripts.
run_command("Setting execute rights on shell scripts...", "chmod u+x *.sh")

# Set an alias to run git-sync.sh.
run_command("Adding git-sync alias...", "echo alias git-sync='git-sync.sh' > /root/.bash_aliases")

# Add evercode-setup directory to PATH variable.
run_command("Adding evercode-setup to PATH...", "sed -i 's/\(PATH=.*\)/\1:\/root\/evercode-setup/' /root/.bash_profile")

# Updating bash session commands.
run_command("Reloading bash session commands...", "source /root/.bashrc")

# Add a symlink to "/var/www/html".
run_command("Adding symlink to public web folder...", "ln -s /var/www/html /root/html")