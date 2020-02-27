import abc

class Transportation(metaclass = abc.ABCMeta):
   """Abstract base class"""

   def __init__( self, start, end, distance ):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def get_start(self):
      return self.start

   def get_end(self):
      return self.end

   def get_distance(self):
      return self.distance
   
   @abc.abstractmethod
   def find_cost( self ):
      """Abstract method; derived classes must override"""
      raise NotImplementedError
   
class Walk(Transportation):
   def __init__(self, start_place = "", end_place = "", distance = 0):
      super().__init__(start_place, end_place, distance)
   def find_cost(self):
      cost = super().get_distance() * 0
##        print ("From " + super().get_start_place() + " to " + super().get_end_place() + ", it will cost " + str(cost) + " Baht by walking")
      return cost

# main program
class Taxi(Transportation):
    def __init__(self, start_place = "", end_place = "", distance = 0):
        super().__init__(start_place, end_place, distance)
    def find_cost(self):
        cost = super().get_distance() * 40
##        return ("From " + super().get_start_place() + " to " + super().get_end_place() + ", it will cost " + str(cost) + " Baht by taking a taxi")
        return cost

class Train(Transportation):
    def __init__(self, start_place = "", end_place = "", distance = 0, stations = 0):
        super().__init__(start_place, end_place, distance)
        self.stations = stations
    def find_cost(self):
        cost = self.stations * 5
##        return ("From " + super().get_start_place() + " to " + super().get_end_place() + ", it will cost " + str(cost) + " Baht by taking a train")
        return cost

travel_cost = 0

trip = [ Walk("KMITL","KMITL SCB Bank",0.6),
         Taxi("KMITL SCB Bank","Ladkrabang Station",5),
         Train("Ladkrabang Station","Payathai Station",40,6),
         Taxi("Payathai Station","The British Council",3) ]

for travel in trip:
   travel_cost += travel.find_cost()
print(travel_cost)
