quest_giver = 0x0000B897
npc1 = 0x0000B896
npc2 = 0x0000B89C
npc3 = 0x0000B899
npc4 = 0x0000B895
npc5 = 0x0000B898
npc6 = 0x0000B894

npc_list = [npc1, npc2, npc3, npc4, npc5, npc6]
rune_gumpIDs = [5, 11, 17, 23, 29, 35, 41]
runebook_gump = 1431013363
recall_pause = 3000

runebook_serial = 0x400C0324

runebook = Items.FindBySerial(runebook_serial)

#Recall to quest giver and accept quest
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[0])
Misc.Pause(recall_pause)
Misc.WaitForContext(quest_giver, 10000)
Misc.ContextReply(quest_giver, 1)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 4)

#Recall to quest npcs and talk to them
for i in range(len(npc_list)):
    Items.UseItem(runebook)
    Gumps.WaitForGump(runebook_gump, 10000)
    Gumps.SendAction(runebook_gump, rune_gumpIDs[i+1])
    Misc.Pause(recall_pause)
    Misc.WaitForContext(npc_list[i], 10000)
    Misc.ContextReply(npc_list[i], 1)

#Recall to quest giver, toggle quest item, and turn-in quest
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[0])
Misc.Pause(recall_pause+250)
quest_item = Items.FindByID(0x09A9, 0x0714, Player.Backpack.Serial)
Misc.WaitForContext(Player.Serial, 10000)
Misc.ContextReply(Player.Serial, 3)
Misc.Pause(250)
Target.TargetExecute(quest_item)
Target.WaitForTarget(10000, False)
Misc.Pause(250)
Target.Cancel( )
Misc.Pause(250)
Misc.WaitForContext(quest_giver, 10000)
Misc.ContextReply(quest_giver, 1)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 8)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 5)