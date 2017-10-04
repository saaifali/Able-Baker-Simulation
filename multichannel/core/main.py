from simulation import *
from test import *

def main():
    # Input data ->Mahdi
    customerInterArrivalTime = [1, 2, 3, 4]
    ableServiceTime = [5, 6, 7, 8]
    bakerServiceTime = [10, 11, 12, 13]
    ableBakerPriority = 0  # If 0 => Able is first if 1 => baker is first if 2 => randomly chosen

    customerCount = 100
    timeLength = 0

    # Data processing  -> MrHs
    count = customerCount
    lili = customerListGenerator(customerInterArrivalTime, ableServiceTime, bakerServiceTime, ableBakerPriority, count)

    # printing output using django -> Mahdi

    test(lili)

    return 0


if __name__ == "__main__" :
    main()