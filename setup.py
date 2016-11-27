# Import the OS module.
import os

# Store the setup version number.
setup_version_number = "1.0.1"

# Begin by writing some version information to file.
print("Saving version number.")
os.system("echo 'EverCode Server from version 1.0.1' > /evercode.version")

# Set execute rights on any shell scripts in the folder.
print("Setting execute rights on shell scripts.")
os.system("chmod +x *.sh")