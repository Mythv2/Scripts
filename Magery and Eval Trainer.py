while True:
    Magery = Player.GetSkillValue('Magery')
    if Magery >= 30:
            Spells.CastMagery('Mana Drain')
            Target.WaitForTarget(4000,False)
            Target.Self()
            Misc.Pause(2000)   
   
    if Magery == Player.GetSkillCap('Magery'):
        Misc.ScriptStopAll()