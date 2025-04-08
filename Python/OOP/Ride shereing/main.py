<<<<<<< HEAD
from Usears import Driver ,Rider ,Ride_Share
=======
from Detailsofusear import Driver ,Rider
from ride import Ride_Share
>>>>>>> c54ab35073e3320eed824c9530bd0ff3aa32b5dd

Uber = Ride_Share("Uber")
mahadi = Rider("M.Mahadi","Mahadi@hasan.com",658564251,"Basundara")
Uber.add_rider(mahadi)
kalam = Driver("Kalam","Kalam@hosen.com",545424245,"Uttara")
Uber.add_Driver(kalam)
mahadi.cash_in(10000)
<<<<<<< HEAD
mahadi.ride_request("Mohammad pur",Uber)
=======
mahadi.ride_request("Mohammad_pur")
>>>>>>> c54ab35073e3320eed824c9530bd0ff3aa32b5dd
mahadi.show_Current_ride()