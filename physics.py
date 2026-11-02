#COS 101 Assignment 
#five Physics Formulas
# Abang-ojie soglad 

def speed (distance,time):
    return distance / time 

def force(mass, acceleration):
    return mass * acceleration

def density (mass, volume):
    return mass / volume

def work_done (force, distance):
    return force * distance

def pressure (force, area):
    return force / area

def main():
    print ("Speed:", speed(100, 2))
    print ("Force:", force(10, 5))
    print ("Density:", density(100, 10))
    print ("Work Done:", work_done(10, 5))
    print ("Pressure:", pressure(10, 2))

if __name__ == "__main__":
    main()

