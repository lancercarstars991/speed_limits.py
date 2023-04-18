def check_speed_limit(speed, limit):
    """Check if a given speed is within the speed limit."""
    if speed <= limit:
        print("You are within the speed limit.")
    else:
        print("You are exceeding the speed limit.")

def main():
    # Sample usage
    speed = 80  # km/hour
    limit = 60  # km/hour
    check_speed_limit(speed, limit)

if __name__ == "__main__":
    main()
