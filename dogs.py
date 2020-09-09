from pdb import set_trace as breakpoint

class Dog():
    def __init__(self, name, age, housebroke=True):
        self.name = name
        self.age = age
        self.housebroke = housebroke
        
    
    def bark(self):
        print(f'{self.name} likes to bark!')
# implementing inheritance between classes
class Beagle(Dog):
    def __init__(self, name, age, housebroke=True, barks_alot=True):
        super().__init__(name, age, housebroke)
        self.barks_alot = barks_alot
    # this fucntion has to be inside of this class so at the runtime can be run
    def bark(self):
        if self.barks_alot == True:
            print(f'{self.name} likes to bark!')
        else:
            print(f'{self.name} hates to bark!')
            
if __name__ == "__main__":

    lucky = Dog('lokey', 3)   # if i take out barks_alot the bark function works          
    spike = Dog('spike', 7) # but if a leave just run the beagle function
    breakpoint()         # or i have to bring this function into the beagle class
