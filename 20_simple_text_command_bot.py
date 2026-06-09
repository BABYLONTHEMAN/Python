# 20_simple_text_command_bot.py
# tiny command system
# like your robot game: collect / status / exit

robot = {
    "naw": "robo3",
    "battery": 100,
    "minerals": 0,
    "working": False
}

while True:
    command = input("command -> ").lower()

    if command == "collect":
        robot["working"] = True
        robot["battery"] = robot["battery"] - 10
        robot["minerals"] = robot["minerals"] + 5
        print(robot["naw"] + " collecting meteor minerals...")

    elif command == "status":
        print("--- ROBOT STATUS ---")
        print("battery -> " + str(robot["battery"]))
        print("minerals -> " + str(robot["minerals"]))
        print("working -> " + str(robot["working"]))

    elif command == "stop":
        robot["working"] = False
        print(robot["naw"] + " stopped")

    elif command == "exit":
        print("bye boss")
        break

    else:
        print("unknown command, try: collect / status / stop / exit")

# TEST:
# command -> collect
# robo3 collecting meteor minerals...
# command -> status
# battery -> 90
# minerals -> 5
# working -> True
