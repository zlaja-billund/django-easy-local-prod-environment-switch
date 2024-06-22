import getopt, sys

argumentList = sys.argv[1:]

# Options
options = "dp"

# Long options
long_options = ["development", "production"]


def replace_text(current, new, path):
    search_text = current

    # creating a variable and storing the text
    # that we want to add
    replace_text = new

    # Opening our text file in read only
    # mode using the open() function
    with open(f'{path}.py', 'r') as file:
        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = file.read()

        # Searching and replacing the text
        # using the replace() function
        data = data.replace(search_text, replace_text)

        # Opening our text file in write only
    # mode to write the replaced content
    with open(f'{path}.py', 'w') as file:
        # Writing the replaced data in our
        # text file
        file.write(data)

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-d", "--development"):
            replace_text('production', 'development', 'manage')
            replace_text('production', 'development', 'core/wsgi') # change path to your wsgi file
            print("Environment changed to development")

        elif currentArgument in ("-p", "--production"):
            replace_text('development', 'production', 'manage')
            replace_text('development', 'production', 'core/wsgi') # change path to your wsgi file
            print("Environment changed to production")

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))




