import time
import sys
#
#
from System.Collections.Generic import List
from System import Byte
#

def find_any(containerSerial, typeArray):
    ret_list = []
    container = Items.FindBySerial(containerSerial)
    if container != None:
        for item in container.Contains:
            if item.ItemID in typeArray:
                ret_list.append(item)
            if item.IsContainer:
                for tmp in find_any(item.Serial, typeArray):
                    ret_list.append(tmp)
    return ret_list
    #
corpse_filter = Items.Filter()
corpse_filter.Enabled = 1
corpse_filter.IsCorpse = 1
corpse_filter.OnGround = 1
corpse_filter.RangeMin = -1
corpse_filter.RangeMax = 8
corpse_filter.Movable = False
corpses = Items.ApplyFilter(corpse_filter)
#
if corpses != None:
    Misc.SendMessage("Starting")    
    claim_command = "[claim"
    #Player.ChatSay(52, claim_command)
    for corpse in corpses: 
        if not Target.HasTarget():
            Player.ChatSay(52, claim_command)
            Misc.Pause(1000)
        if Player.Weight <= Player.MaxWeight:           
           if "None" != claim_command:
                Target.WaitForTarget(1000, True)
                Target.TargetExecute(corpse.Serial)
                Misc.Pause(250)                
else:
    Misc.SendMessage("No Corpses Found")
#
if Target.HasTarget():
    Target.Cancel()