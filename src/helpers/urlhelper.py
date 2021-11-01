"""
Class that allows to list the urls for the GEMINI API
"""


class Urls:
    """
    Property that stores an the base path of the api.
    """
    basePath = None

    """
    Property that stores an the url fragment for ticker v1 for 24hr Vol
    """
    tickerV1for24hrVol = None

    """
    Property that stores an the url fragment for ticker V2
    """
    tickerV2forPriceHistory = None

    """
    Property that stores an the url fragment for tradeHistory
    """
    tradeHistory = None

    """
    Property that stores an the url fragment for all the current symbols
    """
    symbols = None

    """
    Property that stores an the url fragment for the price feed
    """
    priceFeed = None

    """
    Constructor for the Service class.

    Parameters:
    self -- An instantiated object of the Service class.
    """

    def __init__(self):
        self.basePath = "https://api.gemini.com/"
        self.tickerV1for24hrVol = "v1/pubticker/"
        self.tickerV2forPriceHistory = "v2/ticker/"
        self.tradeHistory = "v1/trades/"
        self.symbols = "v1/symbols"
        self.priceFeed = "v1/pricefeed"