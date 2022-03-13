import csv
class Locker:
    couriers = {
        "FedEx" : 1,
        "UPS" : 2,
        "USPS" : 3
    }
    def is_drop_off(self, courierCode):
        for key in self.couriers:
            if self.couriers[key] == courierCode:
                self.courier = key
                return True
        else: return False
    
    def drop_off(self, recepient):
        pass