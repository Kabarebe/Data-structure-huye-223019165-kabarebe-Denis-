from collections import deque

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.species}: {self.name}"

class PetAdoptionCenter:
    def __init__(self):
        self.available_pets = []  
        self.adopted_pets_stack = []  
        self.adoption_requests = deque()  

    def add_pet(self, pet):
        self.available_pets.append(pet)
        print(f"{pet} added to available pets.")

    def adopt_pet(self, pet_name):
        for pet in self.available_pets:
            if pet.name == pet_name:
                self.available_pets.remove(pet)
                self.adopted_pets_stack.append(pet)  
                print(f"{pet} adopted.")
                return
        print(f"Pet {pet_name} not found in available pets.")

    def undo_adoption(self):
        if self.adopted_pets_stack:
            pet = self.adopted_pets_stack.pop()  
            self.available_pets.append(pet)  
            print(f"Adoption of {pet} undone.")
        else:
            print("No recent adoptions to undo.")

    def request_adoption(self, pet_name):
        self.adoption_requests.append(pet_name)
        print(f"Adoption request for {pet_name} added to the queue.")

    def process_adoption_request(self):
        if self.adoption_requests:
            pet_name = self.adoption_requests.popleft()  
            self.adopt_pet(pet_name)  
        else:
            print("No adoption requests in the queue.")

    def display_available_pets(self):
        print("Available Pets:")
        if self.available_pets:
            for pet in self.available_pets:
                print(pet)
        else:
            print("No available pets.")

if __name__ == "__main__":
    center = PetAdoptionCenter()

    
    center.add_pet(Pet("Blue", "Dog"))
    center.add_pet(Pet("linda", "Cat"))
    center.add_pet(Pet("tilapia", "Fish"))
    center.add_pet(Pet("mia", "Dog"))
    center.add_pet(Pet("kessy", "cat"))
    center.add_pet(Pet("dangote", "fish"))
    center.add_pet(Pet("lizza", "bird"))
    center.add_pet(Pet("kasuku", "pigeon"))
    center.add_pet(Pet("niyo", "bird"))

    center.display_available_pets()


    center.adopt_pet("Blue")
    center.adopt_pet("kasuku")
    center.adopt_pet("dangote")
    center.adopt_pet("mia")
    center.display_available_pets()

    
    center.request_adoption("linda")
    center.request_adoption("niyo")
    center.process_adoption_request()
    center.display_available_pets()

    
    center.undo_adoption()
    center.display_available_pets()