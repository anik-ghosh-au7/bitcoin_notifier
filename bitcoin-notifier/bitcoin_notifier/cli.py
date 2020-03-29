#!/usr/bin/python3

import argparse
from .utils import *


# this is the command line interpreter function, that takes arguments from it,
# parses it and then call the run function from utils class and passes this arguments to the parameter of that function
def main():
    parser = argparse.ArgumentParser(description="Bitcoin Notifier")

    parser.add_argument("-i", "--interval", type=int, nargs=1,
                        metavar="interval", default=[1], help="Time interval in minutes")

    parser.add_argument("-t", "--threshold", type=int, nargs=1,
                        metavar="threshold", default=[10000], help="Threshold in USD")

    args = parser.parse_args()

    print('Running Application with time interval of ', args.interval[0], ' and threshold = $', args.threshold[0])
    run(args.threshold, args.interval)


if __name__ == "__main__":
    main()
