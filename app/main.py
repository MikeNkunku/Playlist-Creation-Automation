# Retrieves the arguments passed by user
from sys import argv

# Constants
help_ids = ['-h']

# Secondary functions
## Help handler
def display_help():
    print('This is the display_help part.')

# Main
if __name__ != '__main__' :
    print('Properly name your main file, dumb-ass !')
    exit(1)

first_arg  = argv[1] 
print('First argument : {0}'.format(first_arg))
if first_arg in help_ids :
    display_help()
else :
    print('Yes, yes.')
exit(0)