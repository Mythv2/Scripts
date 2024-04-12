from System.Collections.Generic import List

# SETTINGS 
corpse_ID = 0x2006
chest1_ID = 0x0E7C
chest2_ID = 0x09AB
chest3_ID = 0x0E40
chest4_ID = 0x0E41
nef1_ID = 0x4D0D
nef2_ID = 0x4D0C
MiB_ID = 0x099F
moonstone_ID = 0x0F8B
moonstone_hue = 0x0b94

find_list  = [moonstone_ID, chest1_ID, chest2_ID, chest3_ID, chest4_ID, nef1_ID, nef2_ID,MiB_ID]
hue_list = [moonstone_hue]


# SCRIPT

def findCorpses():
    corpses_filter = Items.Filter()
    corpses_filter.IsCorpse = True # optional
    corpses_filter.OnGround = True # Questionably optional
    corpses_filter.RangeMin = 0 # optional
    corpses_filter.RangeMax = 8 # optoinal
    corpses_filter.Graphics = List[int]([corpse_ID,]) # optional, use item IDs
    corpses_filter.CheckIgnoreObject = True # optional, if you use Misc.IgnoreObject(item) the filter will ignore if true.

    corpse_list = Items.ApplyFilter(corpses_filter) # returns list of items, manipulate list after this as you wish

    return corpse_list

def checkCorpse(corpse):
    for item_to_loot in corpse.Contains:
        shouldLoot = False
        if checkItemByID(item_to_loot, find_list):
            shouldLoot = True
            Misc.SendMessage("Found an item!",32)
            Items.Message(corpse,170,"loot this")
        
            
def checkItemByID(item_to_check, valid_ids):
    if item_to_check.ItemID in find_list:
        return True
    return False


def main(): # define the function
    crps_list = findCorpses()
    for current_corpse in crps_list:
        checkCorpse(current_corpse)
        Misc.Pause(50)    
    Misc.Pause(750)


                
# RUN             
main() #call the function