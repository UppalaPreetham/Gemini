from src.helpers.loghelper import Logger;
from src.alerters.pricechange import PriceChangeAlerter;
from src.alerters.volumechange import VolumeChangeAlerter;
from src.alerters.pricedeviation import PriceDeviationAlerter;
"""
Class that allows to check the alerts
"""


class Alerter:
    """
    Property that store the url references neeeded
    """
    priceChangeAlerter = None;

    """
    Property that store the url references neeeded
    """
    priceDeviationAlerter = None;

    """
    Property that store the url references neeeded
    """
    volumeChangeAlerter = None;

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
        self.logger = Logger();
        self.priceChangeAlerter = PriceChangeAlerter();
        self.priceDeviationAlerter = PriceDeviationAlerter();
        self.volumeChangeAlerter = VolumeChangeAlerter();

    def runChecks(self, curr, deviation, check):
        self.logger.createLogAlert("Running check: " + check, 2)
        self.logger.createLogAlert("Using deviation Threshold: " + deviation, 2)
        self.logger.createLogAlert("Running checks on currency pair: " + curr, 2)

        if check == "pricedev":
            self.priceDeviationAlerter.runChecks(curr, deviation, check)
        if check == "pricechange":
            self.priceChangeAlerter.runChecks(curr, deviation, check)
        if check == "voldev":
            self.volumeChangeAlerter.runChecks(curr, deviation, check)










