import sys

from System.Collections.Generic import List
from System import Byte

def journal_search():
    if Journal.Search("daemonic") == True:
        Journal.Clear()
        Misc.Pause(50)
        return False
    Misc.Pause(100)
    if Journal.Search("chest") == True:
        Journal.Clear()
        Misc.Pause(50)
        return False
    Misc.Pause(100)
    if Journal.Search("crate") == True:
        Journal.Clear()
        Misc.Pause(50)
        return False
    Misc.Pause(100)
    if Journal.Search("box") == True:
        Journal.Clear()
        Misc.Pause(50)
        return False
    else:
        return True

def monster_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs
        

bow = 0x4046FC94
Journal.Clear()
Misc.Pause(500)

while journal_search():
    eligible = monster_list(10)
    if len(eligible) > 0:
        nearest = Mobiles.Select(eligible,'Nearest')
        Player.UnEquipItemByLayer('RightHand')
        Misc.Pause(700)
        Player.EquipItem(bow)
        Misc.Pause(700)
        
        if (Player.HasPrimarySpecial == False): 
            Player.WeaponPrimarySA()
            
        Player.Attack(nearest)
        Misc.Pause(1000)
                
        if Player.BuffsExist('Consecrate Weapon') == False:
            Spells.CastChivalry("Consecrate Weapon")
           
                
        if (Player.HasPrimarySpecial == False): 
            Player.WeaponPrimarySA()
            
        Player.Attack(nearest)
        Misc.Pause(1000)
            
        if (Player.HasPrimarySpecial == False): 
            Player.WeaponPrimarySA()


    else:
        Misc.Pause(1250)
        if Player.CheckLayer('RightHand') == False and Player.CheckLayer('LeftHand') == False:
            rod = Items.FindByID(0x0DC0, 0x0000, Player.Backpack.Serial)
            Player.EquipItem(rod)
            Misc.Pause(1000)
        if Player.GetItemOnLayer('RightHand'):
            if Player.GetItemOnLayer('RightHand').ItemID != 0x0DC0:
                rod = Items.FindByID(0x0DC0, 0x0000, Player.Backpack.Serial)
                Player.UnEquipItemByLayer('LeftHand')
                Misc.Pause(700)
                Player.UnEquipItemByLayer('RightHand')
                Misc.Pause(700)
                Player.EquipItem(rod)
                Misc.Pause(1000)
        if Player.GetItemOnLayer('LeftHand'):
            Player.UnEquipItemByLayer('LeftHand')
            Misc.Pause(700)
            rod = Items.FindByID(0x0DC0, 0x0000, Player.Backpack.Serial)
            Player.EquipItem(rod)
            Misc.Pause(1000)
        Items.UseItem(Player.GetItemOnLayer('RightHand'))
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(Player.Position.X, Player.Position.Y ,(Player.Position.Z-16))
        Misc.Pause(250)

        
Player.UnEquipItemByLayer('RightHand')
Misc.Pause(700)
Player.EquipItem(bow)
