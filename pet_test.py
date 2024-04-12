from System.Collections.Generic import List
from System import Byte, Int32, String

pet_names = ['Rune', 'Freyr']

def pet_list(range, petname):
    pets = Mobiles.Filter()
    pets.Enabled = True
    pets.RangeMax = range
    pets.IsGhost = False
    pets.Name = petname
    pet = Mobiles.ApplyFilter(pets)
    return pet

def healpet1():
    Spells.Cast('Greater Heal')
    Target.WaitForTarget(2000, False)
    Target.TargetExecute(pet1)
    Misc.Pause(3000)
    
def healpet2():
    Spells.Cast('Greater Heal')
    Target.WaitForTarget(2000, False)
    Target.TargetExecute(pet2)
    Misc.Pause(3000)


while True:
    if pet_list(15,pet_names[0]):
        pet1 = pet_list(15,pet_names[0])[0]
        pet1hp_ratio = pet1.Hits/pet1.HitsMax
    else:
        pet1 = False

    if pet_list(15,pet_names[1]):
        pet2 = pet_list(15,pet_names[1])[0]
        pet2hp_ratio = pet2.Hits/pet2.HitsMax
    else:
        pet2 = False

    if pet1:
        if pet1.Poisoned:
            Spells.Cast('Cure')
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(pet1)
            Misc.Pause(500)
            
    if pet2:
        if pet2.Poisoned:
            Spells.Cast('Cure')
            Target.WaitForTarget(1000, False)
            Target.TargetExecute(pet1)
            Misc.Pause(500)
            
    while pet1 and pet2:
        if not pet1.Poisoned and not pet2.Poisoned:
            if pet1hp_ratio < pet2hp_ratio and pet1hp_ratio < 0.8:
                healpet1()
            elif pet2hp_ratio < 0.8:
                healpet2()          
    
    while pet1 and not pet2 and pet1hp_ratio < 0.8 and not pet1.Poisoned:
        healpet1()
        
    while not pet1 and pet2 and pet2hp_ratio < 0.8 and not pet2.Poisoned:
        healpet2() 
        