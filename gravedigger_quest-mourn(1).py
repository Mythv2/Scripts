runebook_serial = 0x4009CC47  #update with your runebook serial
quest_npc = 0x00000D05
vincent = 0x00000D0C
linda = 0x00000D11
rune_gumpIDs = [5, 11, 17, 23, 29, 35, 41]
runebook_gump = 1431013363
recall_pause = 3000

runebook = Items.FindBySerial(runebook_serial)

#Recall to starting NPC and accept quest
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[0])
Misc.Pause(recall_pause)
Misc.WaitForContext(quest_npc, 10000)
Misc.ContextReply(quest_npc, 1)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 4)

#Recall to first monster, wait for player to say (next part)
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[1])
while Journal.Search("next part") == False:
    Misc.Pause(500)
Journal.Clear()

#Recall to second monster, wait for player to say (next part)
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[2])
while Journal.Search("next part") == False:
    Misc.Pause(500)
Journal.Clear()

#Recall to third monster, wait for player to say (next part)
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[3])
while Journal.Search("next part") == False:
    Misc.Pause(500)
Journal.Clear()

#Recall to fourth monster, wait for player to say (next part)
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[4])
while Journal.Search("next part") == False:
    Misc.Pause(500)
Journal.Clear()

#Recall to quest npc, talk to them
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[5])
Misc.Pause(recall_pause)
Misc.WaitForContext(vincent, 10000)
Misc.ContextReply(vincent, 1)

#Recall to quest npc, talk to them
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[6])
Misc.Pause(recall_pause)
Misc.WaitForContext(linda, 10000)
Misc.ContextReply(linda, 1)

#Recall to quest npc, talk to them
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[5])
Misc.Pause(recall_pause)
Misc.WaitForContext(vincent, 10000)
Misc.ContextReply(vincent, 1)

#Recall back to the quest giver, find quest item in pack, toggle quest gump stuff, then target quest item
Items.UseItem(runebook)
Gumps.WaitForGump(runebook_gump, 10000)
Gumps.SendAction(runebook_gump, rune_gumpIDs[0])
Misc.Pause(recall_pause)
Misc.Pause(500)
Misc.WaitForContext(Player.Serial, 10000)
Misc.ContextReply(Player.Serial, 3)
Target.WaitForTarget(10000, False)
Misc.Pause(250)
quest_item = Items.FindByID(0x09A1, 0x0000, Player.Backpack.Serial)
Misc.Pause(250)
Target.TargetExecute(quest_item)
Target.WaitForTarget(10000, False)
Target.Cancel( )
Misc.Pause(250)
Mobiles.UseMobile(quest_npc)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 8)
Gumps.WaitForGump(1280077232, 10000)
Gumps.SendAction(1280077232, 5)