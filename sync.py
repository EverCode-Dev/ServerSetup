import os

# Synchronise with GitHub.
print("Synchronising with GitHub...")

try:
    os.system("git pull")

except:
    print("Unknown error occured: %s" % sys.exc_info()[0])
    
print("Synchronised!")