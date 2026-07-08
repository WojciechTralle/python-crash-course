# exercise 8-14
def make_car(manufacturer, model, **car_info):
    """Build dictionary containing everything 
    we know about the car"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

my_car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(my_car)

