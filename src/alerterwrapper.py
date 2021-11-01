from src.helpers.loghelper import Logger;
from src.helpers.api import AlertApiCaller;
from src.alerters.basealerter import Alerter;

"""
Class that allows to check the alerts
"""


class AlerterWrapper:
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
    alerter = None

    def __init__(self):
        self.alertAPICaller = AlertApiCaller();
        self.logger = Logger();
        self.alerter = Alerter();

    def triggerAlerts(self, currency, type, deviation):
        symbols = [];
        type_of_checks = [];

        if currency == "ALL":
            symbols = self.alertAPICaller.getSymbols();
        else:
            symbols.append(currency)

        if type == "ALL":
            type_of_checks = ["pricedev", "pricechange", "voldev"]
        else:
            type_of_checks.append(type)

        for curr in symbols:
            for check in type_of_checks:
                self.alerter.runChecks(curr, deviation, check)