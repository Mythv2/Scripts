while True:
    Magery = Player.GetSkillValue('Magery')
    
    if Magery >= 30 and Magery < 40 and Player.Mana > 11:
            Spells.CastMagery('Mana Drain')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(2000)   
            
    elif Magery >= 40 and Magery < 63 and Player.Mana > 11:
            Spells.CastMagery('Mana Drain')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(2000) 
            
    elif Magery >= 63 and Magery < 75 and Player.Mana > 11:
            Spells.CastMagery('Invisibility')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(2000)
            
    elif Magery >= 75 and Magery < 100 and Player.Mana > 11:
            Spells.CastMagery('Mana Vampire')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(2000) 
            
            
    if Magery == Player.GetSkillCap('Magery'):
        Misc.ScriptStopAll()
