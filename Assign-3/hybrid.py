from playfair import playfair;
from math import ceil;
import sys;
class hybrid:
    def __init__(self):
        self.opt = sys.argv[1].lower();
        self.pfkey = sys.argv[2].upper();
        self.rwkey = sys.argv[3].upper();
        self.text = sys.argv[4].upper();
        self.check();

    def check(self):
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

    def decrypt(self):
        keyok = self.check_rtkey();
        if keyok:
            self.initializeMat();
            self.rev_transpose();
            self.decrypt_mat();
            playfair().check(self.opt,self.pfkey,self.ct_for_pf);

    def decrypt_mat(self):
        temp_ct = "";
        for i in range(self.row):
            for j in range(self.col):
                tmp = self.rev_mat[i][j];
                if tmp != '$':
                    temp_ct = temp_ct+tmp;
        self.ct_for_pf = temp_ct;
        print("\n\n","\t\t*********  PF Cipher Text *********");
        print("\n\t",temp_ct);

    def rev_transpose(self):
        rwkey_array = [int(x) for x in str(self.rwkey)];
        i = 1;k = 0;
        while i  <= len(rwkey_array):
            pos = rwkey_array.index(i);
            for j in range(self.row):
                if k < len(self.text):
                    self.rev_mat[j][pos] = self.text[k];
                    k = k+1;
            i = i+1;
        self.display(self.rev_mat);

    def initializeMat(self):
        ctlen = len(self.text);
        self.col = len(self.rwkey);
        self.row = int(ceil(ctlen/self.col));
        matrix = [];
        for i in range(self.row):
            tmp = [];
            for j in range(self.col):
                tmp.insert(j,'$');
            matrix.append(tmp);
        self.rev_mat = matrix;

    def transpose(self):
        rwkey_array = [int(x) for x in str(self.rwkey)];
        fin_cipher_text = "";i = 1;
        while i  <= len(rwkey_array):
            pos = rwkey_array.index(i);
            for j in range(self.row):
                fin_cipher_text = fin_cipher_text+self.keyMatrix[j][pos];
            i = i+1;
        self.display(self.keyMatrix);
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

    def display(self,mat):
        print("\n\n","\t\t********* Row Matrix *********\n");
        for i in range(self.row):
            print("\t\t\t  ",end = '');
            for j in range(self.col):
                print(mat[i][j],end = ' ');
            print();
        return;

hybrid();
