from System.Collections.Generic import List
from System import Byte

def monster_list (range):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    fil.IsGhost = False
    fil.Friend = False
    mobs = Mobiles.ApplyFilter(fil)
    return mobs

eligible = monster_list(6)

if len(eligible) > 0:
    nearest = Mobiles.Select(eligible,'Nearest')
    while Mobiles.FindBySerial(nearest.Serial) is not None and Player.DistanceTo(nearest)<=10:
        nearby_enemies_len = len(monster_list(1))
        
        if (Player.HasPrimarySpecial == False): 
            Player.WeaponPrimarySA()
        
        Player.Attack(nearest)
        Misc.Pause(1000)
            
        if Player.BuffsExist('Consecrate Weapon') == False:
            Spells.CastChivalry("Consecrate Weapon")
       
            
        if (Player.HasPrimarySpecial == False): 
            Player.WeaponPrimarySA()
            
                
        if (Player.BuffsExist('Counter Attack') == False): 
            Spells.Cast("Counter Attack")
        
        Player.Attack(nearest)
        Misc.Pause(1000)
        
        if (Player.HasPrimarySpecial == False): 
            Player.WeaponPrimarySA()     
            
        #Spells.Cast('Onslaught')
        #Misc.Pause(1000)


