def main():
    robo1 = Robot()
    print(f"First object id is {id(robo1)}")
    print(f"First object type is {type(robo1)}")
    robo2 = Robot()
    print(f"Second object id is {id(robo2)}")
    print(f"Second object type is {type(robo2)}")
    return "print"

class Robot:
    def __init__(self):
        self.msg1 = "Walking like a robot"
        self.msg2 = "Talking like a robot"

    def walk_file_a_robot(self):
        print (self.msg1)

    def talk_file_a_robot(self):
        print (self.msg2)

if __name__ == "__main__": main()
# if __name__ == main(): main()