import aiml
import os


#Set path for the brain file. This is were all the *.aiml are stored for rapid access.
brain_file="brain.dump"

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml b")

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(brain_file):
    print("Loading from brain file: " + brain_file)
    k.loadBrain(brain_file)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="aiml/*.aiml", commands="load aiml b")
    print("Saving brain file: " + brain_file)
    k.saveBrain(brain_file)

# Loop forever, reading user input from the command
# line and printing robot responses.

while True:
    input_text = input("Human: ")
    if input_text == "quit":
        exit()
    elif input_text == "save":
        k.saveBrain("brain.dump")
    else:
        response_robot = k.respond(input_text) 
        print(response_robot)  