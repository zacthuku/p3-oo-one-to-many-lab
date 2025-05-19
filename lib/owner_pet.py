class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner or None")
        self.owner = owner

        Pet.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
   
    pass