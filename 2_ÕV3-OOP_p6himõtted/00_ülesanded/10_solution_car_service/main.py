from car import Car
from service import Service

if __name__ == '__main__':
    c1 = Car("Red", "Ferrari", 5)
    c2 = Car("Red", "BMW", 3)
    c3 = Car("Red", "Ferrari", 7)
    s1 = Service("Shop", 10)
    print(s1.can_add_to_service_queue(c1))
    print(s1.can_add_to_service_queue(c2))
    print(s1.can_add_to_service_queue(c3))
    s1.add_car_to_service_queue(c1)
    print(s1.can_add_to_service_queue(c1))
    print(s1.can_add_to_service_queue(c2))
    print(s1.can_add_to_service_queue(c3))
