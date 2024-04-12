from System.Collections.Generic import List

loot_names = ['artifact', 'Faraan Dungeon Collection']
gear_props_1 = ['mana leech 7', 'mana leech 8', 'mana leech 9', 'mana leech 10']
gear_props_2 = ['lightning 7', 'lightning 8', 'lightning 9', 'lightning 10']
gear_props_3 = ['fireball 7', 'fireball 8', 'fireball 9', 'fireball 10']
gear_props_4 = ['harm 7', 'harm 8', 'harm 9', 'harm 10']
gold_dest = 0x40234E6F #update with your bag of holding serial
loot_dest = 0x4021328F #update with serial of a bag to place loot
lockpick_bag = 0x40234E6F #update with serial of bag with lockpicks
trash_bag = 0x40234E62 #update with serial of your trash 4 tokens bag
lockpick_ID = 0x14FC
gem_keys = 0x401667BB

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
Organizer.RunOnce("regs", source_chest, loot_dest, 500)
Misc.Pause(250)

source_chest_obj = Items.FindBySerial(source_chest)

for item_to_loot in source_chest_obj.Contains:
    shouldLoot = False
    if checkItemByName(item_to_loot, loot_names):
        shouldLoot = True
    if checkItemByName(item_to_loot, gear_props_1) and checkItemByName(item_to_loot, gear_props_2):
        shouldLoot = True
    if checkItemByName(item_to_loot, gear_props_1) and checkItemByName(item_to_loot, gear_props_3):
        shouldLoot = True
    if checkItemByName(item_to_loot, gear_props_1) and checkItemByName(item_to_loot, gear_props_4):
        shouldLoot = True
    if shouldLoot:
        Items.Move(item_to_loot,loot_dest,-1 ) # -1 -> all, for stackable items
        Misc.Pause(750)
    else:
        Items.Move(item_to_loot,trash_bag,-1)

Misc.WaitForContext(gem_keys, 10000)
Misc.ContextReply(gem_keys, 2)
Gumps.WaitForGump(111922706, 10000)
Gumps.SendAction(111922706, 0)