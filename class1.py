class player ():
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def Pass (self):
        print(self.name, "passes tha ball ")
    
    def pass_2 (self):
        print(self.name, "passes the ball ")

    def shoot (self):
        print(self.name, "shoots the ball ")

    def jump (self):
        print(self.name, "jumps ")
    
    def score (self):
        print(self.name, "scored a Goal ")
    

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Rank: {self.rank}")
       
# Example of using the Player class

player_1 = player(" Casemiro ",31 ,44)
player_2 = player("Kevin De Bruyne ",32 ,3)
player_3 = player(" Jamal Musiala ",20 ,73)
player_4 = player("Herling Haaland ",23,2)
player_5 = player(" kylian Mbappe ",23,1)


# View player information
print("\nPlayer 1:")
player_1.info()
player_1.Pass()

print("\nPlayer 2:")
player_2.info()
player_2.pass_2()

print("\nPlayer 3:")
player_3.info()
player_3.shoot()

print("\nPlayer 4:")
player_4.info()
player_4.jump()

print("\nPlayer 5:")
player_5.info()
player_5.score()



 

