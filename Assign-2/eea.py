import sys;
class EEA:
    """Implementation of Extended Euclidean Algorithm."""

    def __init__(self):
        self.x = int(sys.argv[1]);
        self.y = int(sys.argv[2]);
        self.calc();

    def calc(self):
        self.qs  = [];
        self.gcd = 0;
        self.getQuotient(self.x,self.y);
        if self.gcd != 1:
            print("Numbers are not co-prime. GCD is ",self.gcd);
        else:
            mat = [[1,0],[0,1]];
            index = 0;current = [];
            for i in range(len(self.qs)-1):
                current = self.mul(mat[index+1],self.qs[i]);
                mat.append(self.sub(mat[index],current));
                #print(self.qs);
                index = index + 1;
            print(self.x,"\t---> ",mat[-1][0]);
            print(self.y,"\t---> ",mat[-1][1]);

    def sub(self,a,b):
        temp = []; i = 0;
        while i < 2:
            temp.insert(i,a[i]-b[i]);
            i = i+1;
        return temp;

    def mul(self,list,quo):
        i = 0;temp = [];
        while i <2:
            temp.insert(i,list[i]*quo);
            i = i+1;
        return temp;

    def getQuotient(self,a,b):
        if(b == 0):
            self.gcd = a;
            return;
        else:
            self.qs.append(int(a/b));
            self.getQuotient(b,a%b);

a = EEA();
