from System.Collections.Generic import List

loot_names = ['artifact', 'Faraan Dungeon Collection']
gold_dest = 0x403BA1E6
loot_dest = 0x402BD9DD
lockpick_bag = 0x403BA1E6
trash_bag = 0x402973ED
lockpick_ID = 0x14FC

def checkItemByName(item_to_check, valid_names):
    for name in valid_names:
        if name.lower() in str(item_to_check.Properties).lower():
            return True
    return False

source_chest = Target.PromptTarget('Select Source Container')#Target container to pull from

lockpick = Items.FindByID(lockpick_ID, -1, lockpick_bag)
Items.UseItem(lockpick)
Target.WaitForTarget(250)
Target.TargetExecute(source_chest)
Misc.Pause(250)
Items.UseItem(source_chest)
Misc.Pause(250)
Items.UseItem(source_chest)
Misc.Pause(1000)

Organizer.RunOnce("gold", source_chest, gold_dest, 500)
Misc.Pause(1000)
Organizer.RunOnce("gold", source_chest, gold_dest, 500)
Misc.Pause(250)
Organizer.RunOnce("chest2", source_chest, loot_dest, 500)
Misc.Pause(250)

source_chest_obj = Items.FindBySerial(source_chest)

for item_to_loot in source_chest_obj.Contains:
    shouldLoot = False
    if checkItemByName(item_to_loot, loot_names):
        shouldLoot = True
    if shouldLoot:
        Items.Move(item_to_loot,loot_dest,-1 ) # -1 -> all, for stackable items
        Misc.Pause(750)

Misc.WaitForContext(0x402C01BC, 10000)
Misc.ContextReply(0x402C01BC, 2)
Gumps.WaitForGump(111922706, 10000)
Gumps.SendAction(111922706, 0)