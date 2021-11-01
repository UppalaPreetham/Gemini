from src.helpers.loghelper import Logger;
from src.helpers.api import AlertApiCaller;
from src.utils import *
import numpy as np

"""
Class that allows to check the alerts
"""


class PriceDeviationAlerter:
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

    2019-08-05 16:09:49,789 - AlertingTool - INFO - Getting symbols API Data
2019-08-05 16:09:49,843 - AlertingTool - INFO - Running checks
2019-08-05 16:09:49,843 - AlertingTool - INFO - * Running priceDev check on: zecbch
2019-08-05 16:09:49,843 - AlertingTool - INFO - Getting Price API Data for: zecbch
2019-08-05 16:09:49,858 - AlertingTool - INFO - Last Price: 0.1312
2019-08-05 16:09:49,858 - AlertingTool - INFO - Standard Deviation: 0.0220285943126
2019-08-05 16:09:49,858 - AlertingTool - INFO - Average: 0.1732375
2019-08-05 16:09:49,858 - AlertingTool - INFO - Price diff: 0.0420375
2019-08-05 16:09:49,859 - AlertingTool - ERROR - **   Price Deviation
    """

    def __init__(self):
        self.alertAPICaller = AlertApiCaller();
        self.logger = Logger();

    def runChecks(self, currency, deviation, type):
        self.logger.createLogAlert("Running priceDev check on: " + currency, 2);
        self.logger.createLogAlert("Getting Price API Data for: " + currency, 2);
        last_traded_price = self.alertAPICaller.getLastExecutedPrice(currency)
        self.logger.createLogAlert("Last Price: " + last_traded_price['last'], 2)
        price_history = self.alertAPICaller.get24HourAveragePrices(currency);
        changes = np.array(price_history['changes'])
        changes = np.asfarray(changes, float)
        standard_deviation = stdev(changes)
        self.logger.createLogAlert("Standard Deviation: " + str(standard_deviation), 2)
        average = mean(changes)
        self.logger.createLogAlert("Average: " + str(average), 2)
        price_difference = float(last_traded_price['last']) - average - standard_deviation;
        self.logger.createLogAlert("Price diff: " + str(price_difference), 2)
        if price_difference > 0:
            self.logger.createLogAlert("** Price deviation", 4)

