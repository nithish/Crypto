class playfair:
    """Implementation of Play fair cipher. """
    # def __init__(self,option,key,text):
    #     self.opt = option;
    #     self.key = key;
    #     self.text = text;
        #self.check();

    def check(self,option,key,text):
        self.opt = option;
        self.key = key;
        self.text = text;
        if self.opt == "encrypt":
            return self.encrypt();
        elif self.opt == "decrypt":
            return self.decrypt();
        else:
            print("Invalid Command.");
            print("Syntax: playfair.py [encrypt,decrypt] [key] [plaintext,ciphertext]");
    def encrypt(self):
        self.genMatrix();
        #self.addFiller();
        self.group();
        ct = "";k = self.keyMatrix;
        for i in self.blockText:
            p1 = self.position(i[0]);
            p2 = self.position(i[1]);
            if p1[0] == p2[0]:
                ct = ct+k[p1[0]][(p1[1]+1)%5]+\
                k[p2[0]][(p2[1]+1)%5];
            elif p1[1] == p2[1]:
                ct = ct+k[(p1[0]+1)%5][p1[1]]+\
                k[(p2[0]+1)%5][p2[1]];
            else:
                ct = ct+k[p1[0]][p2[1]]+k[p2[0]][p1[1]];
        print("\n\n","\t\t********* Playfair Cipher Text *********");
        print("\n\t",ct);
        return ct;

    def decrypt(self):
        self.genMatrix();
        #self.addFiller();
        self.group();
        ct = "";k = self.keyMatrix;
        for i in self.blockText:
            p1 = self.position(i[0]);
            p2 = self.position(i[1]);
            if p1[0] == p2[0]:
                ct = ct+k[p1[0]][(p1[1]-1+5)%5]+\
                k[p2[0]][(p2[1]-1+5)%5];
            elif p1[1] == p2[1]:
                ct = ct+k[(p1[0]-1+5)%5][p1[1]]+\
                k[(p2[0]-1+5)%5][p2[1]];
            else:
                ct = ct+k[p1[0]][p2[1]]+k[p2[0]][p1[1]];
        print("\n\n","\t\t********* Plain Text *********");
        print("\n\t",ct);
        return ct;

    def genMatrix(self):
        str = ("A", "B", "C", "D", "E", "F", "G",
         "H", "I", "K", "L", "M", "N", "O", "P", "Q",
         "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
        keyMatrix = [];
        cnt = 0; tmp = [];
        key = tuple(self.key)+str;
        for i in range(5):
            row = [];j = 0;
            while j < 5:
                if key[cnt] not in tmp:
                    tmp.insert(cnt,key[cnt]);
                    row.insert(j,key[cnt]);
                    j = j+1;
                cnt = cnt+1;
            keyMatrix.append(row);
        self.keyMatrix = keyMatrix;
        del tmp;
        self.display();

    def display(self):
        ran = [0,1,2,3,4];
        print("\n\n","\t\t********* Key Matrix *********\n");
        for i in ran:
            print("\t\t\t  ",end = '');
            for j in ran:
                print(self.keyMatrix[i][j],end = ' ');
            print();
        return;

    def group(self):
        pt = self.text;
        s = i = 0;bpt = [];temp = "";prev ="";l = len(pt);
        while i < l:
            if s < 2 and prev != pt[i]:
                temp = temp+pt[i];
                prev = pt[i];
                i = i+1;
                s = s+1;
            elif prev == pt[i]:
                if s%2 == 1:
                    temp = temp+'X';
                    prev = 'X';
                else:
                    temp = temp+pt[i];
                    prev = pt[i];
                    i = i+1;
                s = s+1;
            if s >= 2 or i == l:
                if len(temp) < 2:
                    temp = temp+'X';
                bpt.append(temp);
                temp = "";
                s = 0;
        self.blockText = bpt;
        #print(bpt);
    def addFiller(self):
        pt = list(self.text);
        for i in range(len(pt)-1):
            if pt[i] == pt[i+1]:
                pt.insert(i+1,'X');
        self.text = pt;

    def position(self,x):
        l = range(5);
        res = [];
        for i in l:
            for j in l:
                if x == self.keyMatrix[i][j]:
                        res.append(i);
                        res.append(j);
                        break;
        if not res:
            res.append(-1);
        return res;

#a = playfair("encrypt","MONARCHY","BALLOON");
