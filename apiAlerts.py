import argparse
from src.alerterwrapper import AlerterWrapper
from src.helpers.loghelper import Logger

# Create the parser
my_parser = argparse.ArgumentParser(epilog="Runs checks on API")

# Add the arguments
my_parser.add_argument('-c',
                       '--CURRENCY',
                       help='The currency tradiALLmy default value',
                       default='ALL')
my_parser.add_argument('-d',
                       '--DEVIATION',
                       help='percentage threshold for deviation ch',
                       default='5')
my_parser.add_argument('-t',
                       '--type',
                       help=' The type of check to run, or ALL',
                       default='ALL')

logger = Logger();

logger.createLogAlert("Parsing the arguments", 2)
# Execute the parse_args() method
args = my_parser.parse_args()
"""
Alert trigger.
"""
alertWrapper = AlerterWrapper()

"""
Main function of the application.
"""
if __name__ == "__main__":
    try:
        alertWrapper.triggerAlerts(args.CURRENCY, args.type, args.DEVIATION)
    except:
        logger.createLogAlert("Some unexpected error occurred", 4)
