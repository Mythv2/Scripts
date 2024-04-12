oyster_trap = 0x403D6790    #REPLACE with the serial of your trap!
oyster_knife = 0x403D6791  #REPLACE with the serial of your knife!
oyster_ID = [0xA793]
oyster_ID2 = [0xA792]
trash = [0x0D04, 0x44D4, 0x0C60, 0x44D3, 0x0DD6, 0x44D2, 0x0DBD, 0x0D09, 0x0DBC, 0x136C, 0x0D0A,0x44D1]
pearl_ID = [0x3196]

trash_bag = 0x40234E62
pearl_bag = 0x408E94B8

Journal.Clear()

def journal_search():
    if Journal.Search("**bob**"):
        Misc.Pause(250)
        Journal.Clear()
        return True
    else:
        return False

def ThrowTrap():
    Items.UseItem(oyster_trap)
    Target.WaitForTarget(10000,False)
    Target.TargetExecute(Player.Position.X, Player.Position.Y+1 ,(Player.Position.Z))
    
def UseKnife():
    for i in Player.Backpack.Contains:
        if i.ItemID in oyster_ID:
            Items.UseItem(oyster_knife)
            Target.WaitForTarget(10000,False)
            Target.TargetExecute(i)
            Misc.Pause(250)
    
def TrashOpenOyster():
    for i in Player.Backpack.Contains:
        if i.ItemID in oyster_ID2:
            Items.Move(i,trash_bag,-1)
            Misc.Pause(500)
    
def TrashRemover():
    for i in Player.Backpack.Contains:
        if i.ItemID in trash:
            Items.Move(i,trash_bag,-1)
            Misc.Pause(500)
            
def PearlMover():
    for i in Player.Backpack.Contains:
        if i.ItemID in pearl_ID:
            Items.Move(i,pearl_bag,-1)
            Misc.Pause(500)
            
def main():
    ThrowTrap()
    while journal_search() == False:
        Misc.Pause(500)
    Items.UseItem(oyster_trap)
    Misc.Pause(550)
    Items.UseItem(oyster_trap)
    Misc.Pause(550)
    UseKnife()
    TrashOpenOyster()
    TrashRemover()
    PearlMover()
    Misc.Pause(550)
main()