##Project Summary :


In this project my main aim was to build a python module that would be pip installable and will run as a command line tool to fetch live bitcoin prices from CoinMarketCap API and bundle them to send as a message to a public telegram channel and also a notification to my mobile whenever the price falls beyond a particular threshold.

Together with this I also tried predicting the closing price of Bitcoin for the next one year by implementing time-series analysis on the closing price data from 1st January 2017 by using the ARIMA (Auto Regressive Intregated Moving Average) model.

There’s a detailed explanation of the same in my GitHub link https://github.com/anik-ghosh-au7/bitcoin_notifier/blob/master/Bitcoin_ARIMA.ipynb. The source code for the entire project is also there in the root directory.


In this project I have used IFTTT as the web service provider to create applets to connect my services with the required platform like in this case it’s a public channel in telegram and my mobile device.

I have created two applets for the above mentioned purpose in IFTTT, whose functions are as follows,

	1. 	To get periodic Bitcoin price updates on this public telegrams channel - telegram.me/bitcoin_notifications

	2.	To get emergency notifications on my IFTTT app in my mobile whenever the price falls below a certain threshold which will be given as a command line argument, by default its set to $10000.


Inside the package bitcoin-notifier theres a python module bitcoin_notifier which consits of the __init__.py, utils.py and cli.py file.

The cli.py file has one main() function which takes argument that we give in the command line parses it and assigns it as attributes to an object and passes this as arguments to the run() function in the utils class.

The utils.py file consists of the following functions,

	It assigns a dynamic IFTTT web hook url with my key to the web_hook_url variable, so that we can later manipulate it according to the event that we want to trigger in IFTTT.

	1. get_latest_bitcoin_price() : This function fetches the data from the CoinMarketCap Api using my key, creates a session object udate the headers with the necessary info, uses the get method of requests package and tries to retrives the necessary data from the json file.

	2. post_web_hook() : This function changes the web hook url dynamically according to the events that needs to be triggered, uses the post method to pass this URL and the data in json format to be used by IFTTT to trigger the necessary actions and pass the data as values over there.

	3. format_bitcoin_history() : This function formats the data fetched from the API in correct datetime and price format and making a string obj by concatenating both and then finally append to a list and return the joined elements of the list to the calling function run().

	4. run() : This is the main runner function which is called from the utils.main(), it runs for the time interval and threshold passed as arguments from there.


Other than these files, the pacakge contains the following other files,

	1. README.md : This file contains the installation, uninstallation, help otions, argument option details.

	2. LICENSE : This file contains an open source MIT license with me as the author.

	3. setup.py : This file contains the necessary and otional build details like name, email of the author, url for thesource code of the project, necessary python version and pacages to install this package etc.

	4. MANIFEST.in : This file contains the name of the files that are not inside the module but are part of the package.

there are other build files for the distributions inside this package.




