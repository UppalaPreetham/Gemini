from src.helpers.loghelper import Logger;
from src.helpers.api import AlertApiCaller;
"""
Class that allows to check the alerts
"""


class VolumeChangeAlerter:
    """
    Property that store the url references neeeded
    """
    alertAPICaller = None;

    """
    Property that stores the logger reference
    """
    logger = None
    """
    Constructor for the AlertAPICaller class.

    Parameters:
    self -- An instantiated object of the Service class.
    """

    def __init__(self):
        self.alertAPICaller = AlertApiCaller();
        self.logger = Logger();

    def runChecks(self, currency, deviation, type):
        self.logger.createLogAlert("check on volume change need to be implemented", 2);