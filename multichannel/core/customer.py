DEFAULT = 0

class Customer():
    inter_arrival_time = 0
    arrival_time = 0
    when_able_available = 0
    when_baker_available = 0
    server = DEFAULT
    service_time = 0
    service_begin_time = 0
    able_service_end_time = 0
    baker_service_end_time = 0
    delay = 0
    time_in_system = 0


    def __init__(self,i1=0,i2=0,i3=0,i4=0,i5=0,i6=0,i7=0,i8=0,i9=0,i10=0, i11=0):
        self.inter_arrival_time = i1
        self.arrival_time = i2
        self.when_able_available = i3
        self.when_baker_available = i4
        self.server = i5
        self.service_time = i6
        self.service_begin_time = i7
        self.able_service_end_time = i8
        self.baker_service_end_time = i9
        self.delay = i10
        self.time_in_system = i11