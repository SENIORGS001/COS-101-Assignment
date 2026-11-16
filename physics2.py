
# COS 101 ASSIGNMENT
# PHYSICS OPERATIONS USING FUNCTIONS AND WHILE LOOP

# 1. Speed = Distance / Time
def speed(distance, time):
    return distance / time


# 2. Force = Mass * Acceleration
def force(mass, acceleration):
    return mass * acceleration


# 3. Density = Mass / Volume
def density(mass, volume):
    return mass / volume


# 4. Work Done = Force * Distance
def work_done(force_value, distance):
    return force_value * distance


# 5. Weight = Mass * Gravity
def weight(mass, gravity=9.8):
    return mass * gravity


# Main program
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Density")
    print("4. Calculate Work Done")
    print("5. Calculate Weight")

    choice = input("\nChoose a physics operation (1-5): ")

    if choice == "1":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))

        if time == 0:
            print("Time cannot be zero.")
        else:
            print("Speed =", speed(distance, time), "m/s")

    elif choice == "2":
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))

        print("Force =", force(mass, acceleration), "N")

    elif choice == "3":
        mass = float(input("Enter mass: "))
        volume = float(input("Enter volume: "))

        if volume == 0:
            print("Volume cannot be zero.")
        else:
            print("Density =", density(mass, volume), "kg/m³")

    elif choice == "4":
        force_value = float(input("Enter force: "))
        distance = float(input("Enter distance: "))

        print("Work Done =", work_done(force_value, distance), "J")

    elif choice == "5":
        mass = float(input("Enter mass: "))

        print("Weight =", weight(mass), "N")

    else:
        print("Invalid choice. Please select 1-5.")
00
    continue_program = input(
        "\nDo you want to continue? (yes/no): "
    ).lower()

    if continue_program != "yes":
        print("Thank you for using the Physics Calculator!")
        break
