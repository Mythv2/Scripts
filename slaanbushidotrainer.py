while True:
    Bushido = Player.GetSkillValue('Bushido')
    
    if Bushido >= 30 and Bushido < 60 and Player.Mana > 11:
            Spells.CastBushido('Confidence')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(10000)   
            
    elif Bushido >= 60 and Bushido < 75 and Player.Mana > 11:
            Spells.CastBushido('Counter Attack')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(10000) 
            
    elif Bushido >= 75 and Bushido < 105 and Player.Mana > 11:
            Spells.CastBushido('Evasion')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(10000)
            
    if Bushido == Player.GetSkillCap('Bushido'):
        Player.HeadMessage( colors[ 'green' ], 'Congratulations! You are now GM in Bushido.!' )
        Misc.ScriptStopAll()