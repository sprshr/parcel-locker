import csv
class Locker:
    couriers = {
        "FedEx" : 11111,
        "UPS" : 22222,
        "USPS" : 33333
    }
    def is_drop_off(self, courierCode):
        for key in self.couriers:
            if self.couriers[key] == courierCode:
                self.courier = key
                return True
        else: return False
    
    def drop_off(self, first, last, address, zipCode):
        pass