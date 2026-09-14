class Pet():
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def get_species():
        pet_species = input("Enter the animal species: ")
        return pet_species
    
    def calculate_age(self):
        if self.species == 'Dog':
            human_age = self.age * 7
            return human_age
        elif self.species == 'Cat':
            human_age = 24 + (self.age - 2) * 4
            return human_age
        else:
            return "Idk, the pet you put was too obscure, put cat or dog next time"
    
    def avg_lifespan(self):
        if self.species == 'Dog':
            return "Average lifespan of a dog is 10 to 13 years"
        elif self.species == 'Cat':
            return "Average lifespan of a cat is between 13 and 17 years"
        else:
            return "Average horse lifespan is 25 to 30 years and a fish is 1 to 3. If you put anything else idk"
        
pet1 = Pet('Fido', 4, Pet.get_species())
pet1_age = pet1.calculate_age()
pet1_lifespan = pet1.avg_lifespan()

pet2 = Pet('Bobby', 6, Pet.get_species())
pet2_age = pet2.calculate_age()
pet2_lifespan = pet2.avg_lifespan()

pet3 = Pet('Blubbo', 1, Pet.get_species())
pet3_age = pet3.calculate_age()
pet3_lifespan = pet3.avg_lifespan()

print(f"{pet1.name} is {pet1_age} human years old and the {pet1_lifespan}")
print(f"{pet2.name} is {pet2_age} human years old and the {pet2_lifespan}")
print(f"{pet3.name} is {pet3_age} human years old and the {pet3_lifespan}")



