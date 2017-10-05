from customer import Customer
import random


ABLE = 0
BAKER = 1
RANDOM = 2
DEFAULT = ABLE
SERVERS = [ABLE, BAKER]

def getInterArrivalTime(customerList):
    return random.choice(customerList)


def getServer(previous_customer, priority, arrival_time):
    if priority==ABLE:
        if (previous_customer.able_service_end_time <= arrival_time):
            return ABLE
        else:
            if previous_customer.able_service_end_time <= previous_customer.baker_service_end_time :
                return ABLE
            else:
                return BAKER
    elif priority==BAKER:
        if (previous_customer.baker_service_end_time <= arrival_time):
            return BAKER
        else:
            if previous_customer.baker_service_end_time <= previous_customer.able_service_end_time :
                return BAKER
            else:
                return ABLE
    else :
        return random.choice(SERVERS)


def getServiceTime(server, able_list, baker_list):
    if server == ABLE:
        return random.choice(able_list)
    else:
        return random.choice(baker_list)


def customerListGenerator(customer_time_list, able_list, baker_list, priority, count):
    customer_list = []

    for i in range(count):

        if i==0 : #the first customer
            cust = Customer()
            if priority == RANDOM :
                priority = random.choice(SERVERS)

            service_time = None
            if priority == ABLE :
                service_time = getServiceTime(priority, able_list, baker_list)
                cust.server = ABLE
                cust.able_service_end_time = service_time
            elif priority == BAKER :
                service_time = getServiceTime(priority, able_list, baker_list)
                cust.server = BAKER
                cust.baker_service_end_time = service_time
            cust.service_time = service_time
            cust.time_in_system = service_time
            customer_list.append(cust)

        else : #all following customers
            previous = len(customer_list) - 1
            previous_customer = customer_list[previous]
            inter_arrival_time = getInterArrivalTime(customer_time_list)

            if priority == RANDOM :
                priority = random.choice(SERVERS)

            cust = Customer()

            arrival_time = previous_customer.arrival_time + inter_arrival_time
            server = getServer(previous_customer, priority, arrival_time)
            service_time = getServiceTime(server, able_list, baker_list)
            able_available_at = previous_customer.able_service_end_time
            baker_available_at = previous_customer.baker_service_end_time

            cust.arrival_time = arrival_time
            cust.server = server
            cust.inter_arrival_time = inter_arrival_time
            cust.service_time = service_time
            cust.when_able_available = able_available_at
            cust.when_baker_available = baker_available_at

            delay = None
            service_begins_at = None

            if server == ABLE:
                if arrival_time >= able_available_at:
                    service_begins_at = arrival_time
                    delay = 0
                else:
                    service_begins_at = able_available_at
                    delay = service_begins_at - arrival_time
                cust.able_service_end_time = service_begins_at + service_time
                cust.baker_service_end_time = baker_available_at
                cust.time_in_system = cust.able_service_end_time - cust.arrival_time

            elif server == BAKER:
                if arrival_time >= baker_available_at:
                    service_begins_at = arrival_time
                    delay = 0
                else:
                    service_begins_at = baker_available_at
                    delay = service_begins_at - arrival_time
                cust.able_service_end_time = able_available_at
                cust.baker_service_end_time = service_begins_at + service_time
                cust.time_in_system = cust.baker_service_end_time - cust.arrival_time


            cust.service_begin_time = service_begins_at
            cust.delay = delay
            customer_list.append(cust)

    return customer_list

