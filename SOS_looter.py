from System.Collections.Generic import List

loot_names = ['artifact']
gold_dest = 0x40234E6F
loot_dest = 0x4021328F
trash_dest = 0x40234E62
lockpick_bag = 0x40234E6F
lockpick_ID = 0x14FC

def checkItemByName(item_to_check, valid_names):
    for name in valid_names:
        if name.lower() in str(item_to_check.Properties).lower():
            return True
    return False

source_chest = Target.PromptTarget('Select Source Container')#Target container to pull from

lockpick = Items.FindByID(lockpick_ID, -1, lockpick_bag)
Items.UseItem(lockpick)
Target.WaitForTarget(1000)
Target.TargetExecute(source_chest)
Misc.Pause(250)
Items.UseItem(source_chest)

Organizer.RunOnce("regs", source_chest, gold_dest, 500)
Misc.Pause(250)

source_chest_obj = Items.FindBySerial(source_chest)

for item_to_loot in source_chest_obj.Contains:
    shouldLoot = False
    if checkItemByName(item_to_loot, loot_names):
        shouldLoot = True
    if shouldLoot:
        Items.Move(item_to_loot,loot_dest,-1 ) # -1 -> all, for stackable items
        Misc.Pause(750)
    else:
        Items.Move(item_to_loot,trash_dest,-1)