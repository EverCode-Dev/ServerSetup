from evercode_os import run_command

# Store the setup version number.
setup_version_number = "1.0.1"

# Begin by writing some version information to file.
run_command("Saving version number", "echo 'EverCode Server from version %s' > /evercode.version" % setup_version_number)

# Set execute rights on any shell scripts in the folder.
run_command("Setting execute rights on shell scripts", "chmod u+x *.sh")