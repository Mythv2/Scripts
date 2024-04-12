if (Player.HasSecondarySpecial == False): 
    Player.WeaponSecondarySA()

if Player.BuffsExist('Consecrate Weapon') == False:
    Spells.CastChivalry("Consecrate Weapon")

if Player.BuffsExist('Divine Fury') == False:
    Spells.CastChivalry('Divine Fury')
    Misc.Pause(500)