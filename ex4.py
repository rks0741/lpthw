cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
avarage_passengers_per_car=passengers/cars_driven

print("there are", cars, "cars avaliable")
print("there are only", drivers, "drivers avaliable")
print("there will be ", cars_not_driven, "empty cars today")
print("We have ", passengers, "to carpool today")
print("We need to put about", avarage_passengers_per_car, " passengers in each car")
