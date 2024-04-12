detector = 0x2556

x = Items.FindByID(detector, -1, Player.Backpack.Serial)
Items.SingleClick(x)
Misc.Pause(100)
Misc.WaitForContext(x.Serial, 10000)
Misc.ContextReply(x.Serial, 0)

