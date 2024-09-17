### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 1

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt



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
    stockList = ["AMD", "INTC", "NVDA", "AMC", "GME"]
    #   Converting Stock list to numpy array
    stockList = np.array(stockList)

    createGraphs(stockList)


#   this function takes a np array, stockList, and converts the last 10 closing prices
#   to graphs
def createGraphs(stockList):
    for stock in stockList:
        #   np array of closing prices
        stockClosing = np.array(getClosingList(stock))
        #   sorted array for min/max values
        stockSorted = np.sort(stockClosing)
        days = list(range(1, len(stockClosing) + 1))
        #   creating axis labels & padding (*1.01 for padding)
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
