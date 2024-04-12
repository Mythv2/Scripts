while Player.Mana > 20:
    Spells.CastMagery( 'Energy Bolt' )
    Target.WaitForTarget( 2000, False )
    Target.Last()
    Misc.Pause( 1600 )
    Player.UseSkill( 'Meditation' )
    while Player.Mana < 34:
        Misc.Pause( 100 )
