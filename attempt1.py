from System.Collections.Generic import List

loot_names1 = ['Essence']
loot_names2 = ['Claw']
loot_dest1 = 0x401566B5
loot_dest2 = 0x401566B5
corpse_ID = 0x2006

def checkItemByName(item_to_check, valid_names):
    for name in valid_names:
        if name.lower() in str(item_to_check.Properties).lower():
            return True
    return False
    
def findCorpses():
    corpses_filter = Items.Filter()
    corpses_filter.IsCorpse = True # optional
    corpses_filter.OnGround = True # Questionably optional
    corpses_filter.RangeMin = 0 # optional
    corpses_filter.RangeMax = 8 # optoinal
    corpses_filter.CheckIgnoreObject = True # optional, if you use Misc.IgnoreObject(item) the filter will ignore if true.

    corpse_list = Items.ApplyFilter(corpses_filter) # returns list of items, manipulate list after this as you wish

    return corpse_list

def main(): # define the function
    crps_list = findCorpses()
    for current_corpse in crps_list:
        for item_to_loot in current_corpse.Contains:
            shouldLoot1 = False
            shouldLoot2 = False
            if checkItemByName(item_to_loot, loot_names1):
                shouldLoot1 = True            
            if shouldLoot1:
                Items.Move(item_to_loot,loot_dest1,-1 ) # -1 -> all, for stackable items
                Misc.Pause(500)
            if checkItemByName(item_to_loot, loot_names2):
                shouldLoot2 = True            
            if shouldLoot2:
                Items.Move(item_to_loot,loot_dest2,-1 ) # -1 -> all, for stackable items
                Misc.Pause(500)
    Misc.Pause(750)
    
main()
    

        