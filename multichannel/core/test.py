from copy import deepcopy

def test(lili):
    print "no.\t|\tInterArrivalTime\t|\tArrivalTime\t|\tAbleAvailable\t|\tBakerAvailable\t|\tServer\t|\tServiceTime\t|\tBegin\t|\tAbleEnd\t|\tBakerEnd\t|\tDelay\t|\tTimeInSYstem"
    for i in range(len(lili)):
        k = lili[i]
        print str(i) + "\t|\t\t" + str(k.inter_arrival_time) + "\t\t\t\t|\t\t" + str(k.arrival_time) + "\t\t|\t\t" + str(
            k.when_able_available) + "\t\t\t|\t\t" + str(k.when_baker_available) + "\t\t\t|\t\t" + str(k.server) + "\t|\t\t" + str(
            k.service_time) + "\t\t|\t\t" + str(k.service_begin_time) + "\t|\t\t" + str(
            k.able_service_end_time) + "\t|\t\t" + str(k.baker_service_end_time) + "\t\t|\t\t" + str(
            k.delay) + "\t|\t\t" + str(k.time_in_system) + "\t\t|"

    allData = []
    for i in range(len(lili)):
        k = lili[i]
        s = [str(i), str(k.inter_arrival_time), str(k.arrival_time), str(k.when_able_available), str(k.when_baker_available),
             str(k.server), str(k.service_time), str(k.service_begin_time), str(k.able_service_end_time),
             str(k.baker_service_end_time), str(k.delay), str(k.time_in_system)]
        allData.append(deepcopy(s))
    return allData





