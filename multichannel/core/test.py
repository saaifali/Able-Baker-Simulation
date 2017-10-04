def test(lili):
    for i in range(len(lili)):
        k = lili[i]
        print str(i) + "  |  " + str(k.inter_arrival_time) + "  |  " + str(k.arrival_time) + "  |  " + str(
            k.when_able_available) + "  |  " + str(k.when_baker_available) + "  |  " + str(k.server) + "  |  " + str(
            k.service_time) + "  |  " + str(k.service_begin_time) + "  |  " + str(
            k.able_service_end_time) + "  |  " + str(k.baker_service_end_time) + "  |  " + str(
            k.delay) + "  |  " + str(k.time_in_system) + "  |  ";
