# Bitcoin Notifier

A Python package to get bitcoin price notifications & predictions.

## Installation

Following command on terminal will install bitcoin-notifier package/module from PIP

```
pip3 install bitcoin-notifier
```
Following command on terminal will install the latest bitcoin-notifier package/module from PIP

```
pip3 install -U bitcoin-notifier
```

## Usage

Following query on terminal will provide you with all the help options available 

##### Input :

```
bitcoin-notifier -h
```

##### Output :

```
usage: bitcoin-notifier [-h] [-i interval] [-t threshold]
Bitcoin Notifier
optional arguments:
  -h, --help            show this help message and exit
  -i interval, --interval interval
                        Time interval in minutes
  -t threshold, --threshold threshold
                        Threshold in USD
```

Following query on terminal will provide you five prices of Bitcoin at a time at one min interval and whenever it falls below $10000 and emergency notification will be sent.

```
bitcoin-notifier -i delhi -t 10000
```

## Un-installation

Following command on terminal will uninstall bitcoin-notifier package/module from your device

```
pip3 uninstall bitcoin-notifier
```

### Join this telegram channel to get the updates :

Following is the invite link

```
telegram.me/bitcoin_notifications
```