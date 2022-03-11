class Locker:
    def __init__(self):
        self.couriers ={
            "FedEx" : 1,
            "UPS" : 2,
            "USPS" : 3
        }

    def drop_off(self, courierCode):
        for key in self.couriers:
            if self.couriers[key] == courierCode:
                break
                return key
            else: return False
