class first(object):
    """docstring for first."""
    def __init__(self):
        #self.arg = arg
        print("Hello")

r = first()

def addFiller(self):
    pt = list(self.text);
    for i in range(len(pt)-1):
        if pt[i] == pt[i+1]:
            pt.insert(i+1,'X');
    self.text = pt;


    def addFiller(self):
        pt = self.blockText;tmp = "";
        for i in range(len(pt)):
            if pt[i][1] == pt[i][2]:
                tmp = pt[i][2];
                pt[i][2] = 'X';
            #if tmp:

        self.text = pt;
