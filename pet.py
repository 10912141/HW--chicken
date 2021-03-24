from random import randrange

class Pet(object):
    """pet"""
    ex_reduce = 3
    ex_max = 10
    ex_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vo = ['"rrrr..."','"Hi"']
    
    def __init__(self,name,animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.ex = randrange(self.ex_max)
        self.vo = self.vo[:]

    def __clock__tick(self):
        self.ex -= 1
        self.food -= 1


    def emotion(self):
        if self.food > self.food_warning and self.ex > self.ex_warning:
            return"Happy!!"
        elif self.food < self.food_warning:
            return"Angury!!I'm hungry"
        else :
            return"I'm bored"

    def __str__(self):
        return"\nI'm" + self.name +"."+"\nI feel" +self.emotion() +"."

    def teach(self,word):
        self.vo.append(word)
        self.__clock__tick()

    def talk(self):
        print(
            "I'm a" , 
            self.animal_type,
            "named",
            self.name,
            "."
        )
        print(self.vo[randrange(len(self.vo))])
        self.__clock__tick()

    def feed(self):
        print("...... \n mmm. Thank you")
        meal = randrange(0,self.food_max)
        self.food += meal

        if self.food <0:
            self.food = 0
            print("I'm still hungry")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I'm full")
        self.__clock__tick()
    
    def play(self):
        print("RRRRRR")
        fun = randrange(0,self.ex_max)
        self.ex += fun
        if self.ex <0:
            self.ex = 0
            print("I'm bored")
        elif self.ex >= self.ex_max:
            self.ex = self.ex_max
            print("I'm so happy")
        self.__clock__tick()

def main():
    pet_name = input("What is your pet name?")
    pet_type = input("What type of  animal is your pet?" )

    my_pet = Pet(pet_name,pet_type)

    input(
        "Hello! I'm " +
         my_pet.name +
         "and I'm here"
         "\n Press enter"
    )

    choice = None

    while choice != 0:
         print("""

         1 -feed
         2 -talk
         3 -teach
         4 -play
         5 -Quit 

         """ )

         choice = input("Choice:")
  
         if choice =="5":
                print("bye")
                break
         elif choice =="1":
                my_pet.feed()
         elif choice =="2":
                my_pet.talk()
         elif choice =="3":
                new_word = input("What do want to teach your pet to say?")
                my_pet.teach(new_word)
         elif choice =="4":
                my_pet.play()
         else:
                print("error")



main() 





