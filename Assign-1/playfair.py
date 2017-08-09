import sys;
class playfair:
    """Implementation of Play fair cipher. """
    def __init__(self):
        self.opt = sys.argv[1];
        self.key = sys.argv[2];
        self.text = sys.argv[3];
        self.check();

    def check(self):
        if self.opt == "encrypt":
            self.encrypt();
        elif self.opt == "decrypt":
            self.decrypt();
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
                ct = ct+k[p1[0]][(p1[1]+1)%6]+\
                k[p2[0]][(p2[1]+1)%6];
            elif p1[1] == p2[1]:
                ct = ct+k[(p1[0]+1)%6][p1[1]]+\
                k[(p2[0]+1)%6][p2[1]];
            else:
                ct = ct+k[p1[0]][p2[1]]+k[p2[0]][p1[1]];
        print("\n\n","\t\t********* Cipher Text *********");
        print("\n\t",ct);

    def decrypt(self):
        self.genMatrix();
        #self.addFiller();
        self.group();
        ct = "";k = self.keyMatrix;
        for i in self.blockText:
            p1 = self.position(i[0]);
            p2 = self.position(i[1]);
            if p1[0] == p2[0]:
                ct = ct+k[p1[0]][(p1[1]-1+6)%6]+\
                k[p2[0]][(p2[1]-1+6)%6];
            elif p1[1] == p2[1]:
                ct = ct+k[(p1[0]-1+6)%6][p1[1]]+\
                k[(p2[0]-1+6)%6][p2[1]];
            else:
                ct = ct+k[p1[0]][p2[1]]+k[p2[0]][p1[1]];
        print("\n\n","\t\t********* Plain Text *********");
        print("\n\t",ct);

    def genMatrix(self):
        str = ("A", "B", "C", "D", "E", "F", "G",
         "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
         "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
        keyMatrix = [];
        cnt = 0; tmp = [];
        key = tuple(self.key)+str;
        for i in range(6):
            row = [];j = 0;
            while j < 6:
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
        ran = [0,1,2,3,4,5];
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
        print(bpt);
    def addFiller(self):
        pt = list(self.text);
        for i in range(len(pt)-1):
            if pt[i] == pt[i+1]:
                pt.insert(i+1,'X');
        self.text = pt;

    def position(self,x):
        l = range(6);
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

a = playfair();
