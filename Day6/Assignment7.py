def traffic_light(color, speed=0):
    match color:
        case 'red':
            print("Stop")
        case 'yellow':
            print("Prepare to stop")
        case 'green':
            if speed > 60:
                print("Slow down even on green")
            else:
                print("Go")
        case _:
            print("Invalid color")


# Test cases
traffic_light('red')
traffic_light('yellow')
traffic_light('green')
traffic_light('green', 70)
traffic_light('blue')