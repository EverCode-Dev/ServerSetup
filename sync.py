from evercode_os import run_command

# Synchronise with GitHub - useful for testing new scripts without a complete
# server wipe and reset.
run_command("Synchronising with GitHub...", "git pull")