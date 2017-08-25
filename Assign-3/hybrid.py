from playfair import playfair;
from math import ceil;
import sys;
class hybrid:
    def __init__(self):
        self.opt = sys.argv[1];
        self.pfkey = sys.argv[2];
        self.rwkey = sys.argv[3];
        self.text = sys.argv[4];
        self.check();

    def check(self):
        print(self.opt);
        if self.opt == "encrypt":
            self.encrypt();
        elif self.opt == "decrypt":
            self.decrypt();
        else:
            print("Invalid Command.");
            print("Syntax: playfair.py [encrypt,decrypt] [key1] [key2] [plaintext,ciphertext]");

    def encrypt(self):
        self.pfcipher = playfair().check(self.opt,self.pfkey,self.text);
        keyok = self.check_rtkey();
        if keyok:
            self.fill_matrix();
            self.transpose();

    def transpose(self):
        rwkey_array = [int(x) for x in str(self.rwkey)];
        fin_cipher_text = "";i = 1;
        while i  <= len(rwkey_array):
            pos = rwkey_array.index(i);
            for j in range(self.row):
                fin_cipher_text = fin_cipher_text+self.keyMatrix[j][pos];
            i = i+1;
        self.display();
        print("\n\n","\t\t********* Final Cipher Text *********");
        print("\n\t",fin_cipher_text);

    def fill_matrix(self):
        matrix = [];k = 0;
        pflen = len(self.pfcipher);
        col = len(self.rwkey);
        row = int(ceil(pflen/col));
        for i in range(row):
            tmp = [];
            for j in range(col):
                if k < pflen:
                    tmp.insert(j,self.pfcipher[k]);
                    k = k+1;
                else:
                    tmp.insert(j,'$');
            matrix.append(tmp);
            tmp = [];
        self.keyMatrix = matrix;
        self.col = col;
        self.row = row;

    def check_rtkey(self):
        klen = len(self.rwkey);
        flag = 1;
        if klen <= 9:
            for i in range(klen):
                if int(self.rwkey[i]) > 9:
                    flag = 0;
                    break;
        else:
            flag = 0;
        return flag;

    def display(self):
        print("\n\n","\t\t********* Row Matrix *********\n");
        for i in range(self.row):
            print("\t\t\t  ",end = '');
            for j in range(self.col):
                print(self.keyMatrix[i][j],end = ' ');
            print();
        return;

hybrid();
