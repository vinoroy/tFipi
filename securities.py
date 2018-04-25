
"""
@author: Vincent Roy [D]

This module implements the concrete securities classes

"""



from asset import *
from pandas_datareader import data as pdr
import datetime
from bs4 import BeautifulSoup



class Security(Asset):
    """
    This class is the abstract securities class that is the superclass of all securities type assets

    Attributes :


    """


    def __init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType):
        Asset.__init__(self, assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType)



class Equity(Security):
    """
    This class is the abstract equity class that is the superclass of all equities type assets

    Attributes :


    """

    def __init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType):
        Security.__init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType)



class CommonStock(Equity):
    """
    This class implements a concrete common stock class that is a child of the equity class


    Attributes :

        - none


    """

    def __init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType):
        Equity.__init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType)
        self.assetType = 'COMMON'


    def getHistoricalPrice(self, startDate, endDate):
        """
        Gets the historical prices (open, low, high, close, adj close and volume) between a set of dates 

        Args :
        - startDate : (string) start date of the extraction (format YY-MM-DD)
        - endDate : (string) end date of the extraction (format YY-MM-DD)

        Return :
            - (Dataframe) open, low, high, close, adj close and volume matrix between a set of dates 
        """

        # try to get the values from the yahoo finance api
        try :
            histValues = pdr.DataReader(self.ticker, data_source='yahoo', start=startDate,end=endDate)

            return histValues

        except:

            return None





class PreferredStock(Equity):
    """
    This class implements a concrete preferred stock class that is a child of the equity class


    Attributes :

        - none


    """

    def __init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType):
        Equity.__init__(self,assetID, purchaseDate, purchasePrice, saleDate, salePrice, volume, percentOwnership,ticker,feedType)
        self.assetType = 'PREFERRED'






    def getHistoricalPrice(self, startDate, endDate):
        """
        Gets the historical prices (open, low, high, close, adj close and volume) between a set of dates 

        Args :
        - startDate : (string) start date of the extraction (format YY-MM-DD)
        - endDate : (string) end date of the extraction (format YY-MM-DD)

        Return :
            - (Dataframe) open, low, high, close, adj close and volume matrix between a set of dates 
        """


        if self.feedType == 'preferredstockchannel':

            pass

        elif self.feedType == 'tmxmoney':

            pass











