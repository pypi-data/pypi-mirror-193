class PD_Data:
    Site_Folder = site = ['SekteDoujin', 'Dojing', 'KumaPoi', 'QinImg', 'KomikLokal', "ManyToon"]

    def __init__(self, ar, n=None):
        self.Thread = ar.thread
        self.URL = ar.link
        self.html = n
        self.Site_Num = n
        self.Site_Dir = n
        self.Ch_Number = n
        self.Ch_Type = n
        self.Bar = n
        self.Width = n
        self.Qin_Multi = False
        self.Root_Dir = n
        self.Slash = n

    def Get_OS(self, name):
        if name == "nt":
            self.Slash = '\\'
        elif name == "posix":
            self.Slash = '/'
        else:
            print("You got a really weird OS")
            raise SystemExit(0)