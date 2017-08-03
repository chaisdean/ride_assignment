class bike(object):

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print self.price
        #self.max_speed = max_speed + 10
        print self.max_speed
        print self.miles

    def ride(self):
        self.miles = self.miles + 10


    def reverse(self):
        self.miles = self.miles - 5

ride1 = bike(299.99, 25)
ride1.ride()
ride1.ride()
ride1.ride()
ride1.reverse()
ride1.displayinfo()

ride2 = ride1
ride2.ride()
ride2.ride()
ride2.reverse()
ride2.reverse()
ride2.displayinfo()

ride3 = ride2
ride3.reverse()
ride3.reverse()
ride3.reverse()
ride3.displayinfo()
