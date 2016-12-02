# Import the run_command function.
from evercode_os import run_command

# Import chdir from os to change the CWD.
from os import chdir

# Import the sys module to get arguments.
import sys

# Output the script name.
print(sys.argv[0])

# Get the name of the config file we will use to setup this server.
print("Reading config file...")
if len(sys.argv) < 2:
    print("No config file was found, stopping.")
    sys.exit
    
setup_config_file_name = sys.argv[1]

# Open the config file and read the contents.
setup_config_file = open(setup_config_file_name, "r")

# Store the config variables.
setup_version_number = setup_config_file.readline()
ftp_html_password    = setup_config_file.readline()
ftp_git_password     = setup_config_file.readline()

# Close the file.
setup_config_file.close()

# Start the setup.
print("Running EverCode Server Setup version %s" % setup_version_number)

# Save the version number to root.
run_command(
    "Saving version number...", 
    "echo 'EverCode Server from setup script version %s' > /evercode.version" % setup_version_number, 
    "cat /evercode.version"
)

# Set execute rights on shell scripts.
run_command(
    "Setting execute rights on shell scripts...", 
    "chmod u+x *.sh"
)

# Set an alias to run git-sync.sh.
run_command(
    "Adding git-sync alias...", 
    "echo alias git-sync='git-sync.sh' > /root/.bash_aliases", 
    "cat /root/.bash_aliases"
)

# Add evercode-setup directory to PATH variable.
run_command(
    "Adding evercode-setup to PATH...", 
    "sed -i 's/\(PATH=.*\)/\1:\/root\/evercode-setup/' /root/.bash_profile", 
    "cat /root/.bash_profile"
)

# Updating bash session commands.
run_command(
    "Reloading bash session commands...",
    "source /root/.bashrc"
)

# Add a symlink to "/var/www/html".
run_command(
    "Adding symlink to public web folder...", 
    "ln -s /var/www/html /root/html"
)

# Add evercode group.
run_command(
    "Adding evercode group...",
    "groupadd evercode"
)

# Setup ProFTPD.
run_command(
    "Setting up ProFTPD...", 
    " && ".join(
        "useradd evercodeftp -M -s /sbin/nologin -d /var/www/html",
        "echo " + ftp_html_password + " | passwd evercodeftp --stdin", 
        "usermod -a -G evercode evercodeftp", 
        "rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm", 
        "yum -y install proftpd", 
        "yum -y install ftp", 
        "sed -i 's/^\( *Umask.*\)[0-9]\{3,4\}$/\1022/' /etc/proftpd.conf", 
        "setsebool -P ftp_home_dir on", 
        "service proftpd start"
    )
)