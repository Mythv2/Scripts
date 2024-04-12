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

eligible = monster_list(8)

if len(eligible) > 0:
    nearest = Mobiles.Select(eligible,'Nearest')
    Player.InvokeVirtue("Honor")
    Target.WaitForTarget(1000)
    Target.TargetExecute(nearest)

    Misc.Pause(750)