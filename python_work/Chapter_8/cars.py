def make_car(manufacturer, model_name, **car_info):
    """store info about a car"""
    car_info['manufacturer'] = manufacturer
    car_info['name'] = model_name
    return car_info

car_profile1 = make_car('Toyota','corolla',year=2021,color='gray')
print(car_profile1)