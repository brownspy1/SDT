from Usears import Driver ,Rider ,Ride_Share

Uber = Ride_Share("Uber")
mahadi = Rider("M.Mahadi","Mahadi@hasan.com",658564251,"Basundara")
Uber.add_rider(mahadi)
kalam = Driver("Kalam","Kalam@hosen.com",545424245,"Uttara")
Uber.add_Driver(kalam)
mahadi.cash_in(10000)
mahadi.ride_request("Mohammad pur",Uber)
mahadi.show_Current_ride()