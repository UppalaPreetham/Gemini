from src.helpers.apihelper import ApiHelper;
from src.helpers.urlhelper import Urls;
"""
Class that allows to call the operations required for API
"""


class AlertApiCaller:
    """
    Property that store the url references neeeded
    """
    urls = None;

    """
    Property that stores the api helper reference
    """
    apiHelper = None

    """
    Constructor for the AlertAPICaller class.

    Parameters:
    self -- An instantiated object of the Service class.
    """

    def __init__(self):
        self.urls = Urls();
        self.apiHelper = ApiHelper();

    def getSymbols(self):
        return self.apiHelper.getDetails(self.urls.basePath+self.urls.symbols)

    def getLastExecutedPrice(self, currency):
        return self.apiHelper.getDetails(self.urls.basePath+self.urls.tickerV1for24hrVol+currency)

    def get24HourAveragePrices(self, currency):
        return self.apiHelper.getDetails(self.urls.basePath+self.urls.tickerV2forPriceHistory+ currency)




