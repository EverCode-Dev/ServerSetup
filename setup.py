# Import custom os functions, standard os and sys.
import evercode_os
import os
import sys

# Get the script name.
local_script_name = sys.argv[0]
evercode_os.print_message("Running from: '%s'" % local_script_name)

# Set the local directory to the script folder.
local_script_directory = local_script_name.replace("setup.py", "")
os.chdir(local_script_directory)

# Get the name of the config file we will use to setup this server.
evercode_os.print_message("Reading config file...")
if len(sys.argv) < 2:
    evercode_os.print_message("No config file was found, stopping.")
    sys.exit()
    
setup_config_file_name = sys.argv[1]
evercode_os.print_message("Using '%s' for setup configuration." % setup_config_file_name)

# Open the config file and read the contents.
try:
    setup_config_file = open(setup_config_file_name, "r")
except:
    evercode_os.print_message("Could not open file '%s', stopping." % setup_config_file_name)
    sys.exit()

# Store the config variables.
setup_version_number = setup_config_file.readline().strip()
ftp_html_password    = setup_config_file.readline().strip()
ftp_git_password     = setup_config_file.readline().strip()

# Close the file.
setup_config_file.close()

# Start the setup.
evercode_os.print_message("Running EverCode Server Setup version %s" % setup_version_number)

# Save the version number to root.
evercode_os.run_command(
    "Saving version number...", 
    "echo 'EverCode Server from setup script version %s' > /evercode.version" % setup_version_number
)

# Set up Git options.
evercode_os.run_command(
    "Setting Git config options...",
    " && ".join([
        "git config --global user.name 'EverCode'",
        "git config --global user.email 'git@evercode.co'",
        "git config --global color.ui auto"
    ])
)

'''# Set execute rights on shell scripts.
run_command(
    "Setting execute rights on shell scripts...", 
    "chmod u+x *.sh"
)

# Set an alias to run git-sync.sh.
run_command(
    "Adding git-sync alias...", 
    r"echo alias git-sync='git-sync.sh' > /root/.bash_aliases", 
    "cat /root/.bash_aliases"
)

# Add evercode-setup directory to PATH variable.
run_command(
    "Adding evercode-setup to PATH...", 
    r"sed -i 's/\(PATH=.*\)/\1:\/root\/evercode-setup/' /root/.bash_profile", 
    "cat /root/.bash_profile"
)

# Updating bash session commands.
run_command(
    "Reloading bash session commands...",
    "source /root/.bashrc"
)'''

# Add a symlink to "/var/www/html".
evercode_os.run_command(
    "Adding symlink to public web folder...", 
    "ln -s /var/www/html /root/html"
)

# Add evercode group.
evercode_os.run_command(
    "Adding evercode group...",
    "groupadd evercode"
)

# Setup a user-password-home map for FTP users.
ftp_username_password_home_map = [
    ["evercodeftp", ftp_html_password, "/var/www/html"       ],
    ["evercodegit", ftp_git_password,  local_script_directory]
]

# Loop over the user-password-home map to add the users.
for user in ftp_username_password_home_map:
    username = user[0]
    password = user[1]
    home     = user[2]
    
    # Add this user.
    evercode_os.run_command(
        "Adding user '%s'..." % username,
        " && ".join([
            "useradd %s -M -s /sbin/nologin -d %s" % (username, home),
            "echo %s | passwd %s --stdin" % (password, username),
            "usermod -a -G evercode %s" % username
        ])
    )

# Setup ProFTPD.
evercode_os.run_command(
    "Setting up ProFTPD...", 
    " && ".join([
        "rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm", 
        "yum -y install proftpd", 
        "yum -y install ftp", 
        "sed -i 's/^\( *Umask.*\)[0-9]\{3,4\}$/\1022/' /etc/proftpd.conf", 
        "setsebool -P ftp_home_dir on", 
        "service proftpd start"
    ])
)
