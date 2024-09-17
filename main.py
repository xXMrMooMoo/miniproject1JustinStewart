### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 1

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import os



#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.



def main():

    createChartFolder()
    stockList = getStocks(5)
    #stockList = ["AMD", "INTC", "NVDA", "AMC", "GME"]
    #   Converting Stock list to numpy array
    stockList = np.array(stockList)

    createGraphs(stockList)

#   user input to get stocks.
def getStocks(amount):
    stockList = []
    for i in range(1,amount+1):
        stock = input(f"Please input stock {i}:").strip().upper()
        #   Will re-prompt user until a valid stock is entered.
        while True:
            response = yf.Ticker(stock)
            try:
                #   checks to see if the dictionary is valid and has a city.
                city_validation = response.info['city']
                #   checks to see the number of data entries, must be equal to or above 10 for the program to work correctly
                #   FSD is an example of a stock that will break most programs.
                history_validation = response.history(period="1mo")
                if len(history_validation) < 10:
                    raise ValueError

                print(f"Valid stock: {stock}")
                #   add to stock list
                if stock in stockList:
                    stock = input(f"Stock {stock} already added. Please re-enter stock {i}:")
                else:
                    stockList.append(stock)
                    break
            except:
                stock = input(f"Stock {stock} is invalid. Please re-enter stock {i}:").strip().upper()
    return stockList



def createChartFolder():
    if os.path.exists("charts") == False:
        os.mkdir("charts")

#   this function takes a np array, stockList, and converts the last 10 closing prices
#   to graphs
def createGraphs(stockList):
    for stock in stockList:
        #   np array of closing prices
        stockClosing = np.array(getClosingList(stock))
        #   sorted array for min/max values
        stockSorted = np.sort(stockClosing)
        days = list(range(1, len(stockClosing) + 1))
        #   creating axis labels & padding
        plt.axis([1, 10, (stockSorted[0] - 1), (stockSorted[-1] + 1)])

        #   plotting and formatting graph.
        plt.plot(days, stockClosing)
        plt.xlabel('Days')
        plt.title(f"Closing Price for {stock}")
        plt.ylabel('Price (USD)')
        plt.savefig(f'charts/{stock}.png')
        plt.show()

#   function to return the last 10 days of a stocks closing price.
def getClosingList(stock):

    closingList = []
    stock_info = yf.Ticker(stock)
    stock_history = stock_info.history(period="1mo")

    #   df of last 10 days
    tenDays = stock_history[-10:]

    for price in tenDays["Close"]:
        closingList.append(round(price, 2))

    return closingList


if __name__ == "__main__":
    main()
