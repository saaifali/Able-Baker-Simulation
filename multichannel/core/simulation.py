from customer import Customer
import random
import server

def getInterArrivalTime(customerList):
    return random.choice(customerList)

def getAbleOrBaker(ableAvailTime,bakerAvailTime,priority):
    if(ableAvailTime == bakerAvailTime):
        if(priority == server.RANDOM):
            return random.choice(server.SERVERS)
        else:
            return priority
    else:
        if(ableAvailTime < bakerAvailTime):
            return server.ABLE
        else:
            return server.BAKER







def customer_generator(customer_time_list, able_list, baker_list, priority, count):
    customer_list = []

    for i in range(count):
        cust = Customer()

        if i==0 : #the first customer
            if priority == server.RANDOM :
                priority = random.choice(server.SERVERS)

            if priority == server.ABLE :
                service_time = random.choice(able_list)
                cust.server = server.ABLE
                cust.service_time = service_time
                customer_list.append()

