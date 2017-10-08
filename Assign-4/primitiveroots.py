from primefactors import primefactors;
from gcd import GCD;
import sys;
class primitiveroots:
    """Syntax: py primitiveroots.py <group size>"""
    def __init__(self):
        self.pf_dict = primefactors();
        self.grpSize = int(sys.argv[1]);
        self.get_proots();

    def get_proots(self):
        self.calc_phi();
        self.calc_prime_pow();
        self.find_proots();

    def find_proots(self):
        i = 2;pr = [];
        # if self.pf_dict.get_factors(self.grpSize) == -1:
        #     while i < self.grpSize:
        #         flag = 0;
        #         for j in range(len(self.prime_pow)):
        #             res = (i**self.prime_pow[j])%self.grpSize;
        #             #print(i,res,self.prime_pow[j]);s
        #             if res != 1:
        #                 flag = flag+1;
        #         if flag == len(self.prime_pow):
        #             pr = i;
        #             break;
        #         i = i+1;
        # else:
            # When the group size is composite number, else block (line no:30)
            # executed which has worst case complexity of O(n^2)
        g = GCD(); elem = [];
        i = 1;
        while i < self.grpSize:
            if g._gcd(i,self.grpSize) == 1:
                elem.append(i);#contains elements of the group whose gcd(e,p) = 1
            i = i+1;
        print("Elements of the group are: ",elem);
        print("Powers of elements\n");
        for i in range(len(elem)):
            n = elem[i];prev = [];
            if n != 1:
                j = 1;
                print("",n,end = "\t");
                while j <= self.phi_val:
                    y = (n**j)%self.grpSize;
                    print(y,end ="\t");
                    #checks whether residue(y) is a element of the group and
                    #also checks the residue is not calculated previously(repeated)
                    if y in elem and y not in prev:
                        prev.append(y);
                    if len(prev) == len(elem) and n not in pr:
                        pr.append(n);
                    j = j+1;
                print();
        print("\nPrimitive roots are: ",pr) if len(pr) > 0  else print("\nNo primitive root for this group");
        print("\n");

    def calc_prime_pow(self):
        pf_phi = self.pf_dict.get_factors(self.phi_val);
        self.prime_pow = []; prev = [];
        if pf_phi != -1:
            for i in range(len(pf_phi)):
                n = pf_phi[i];
                if n not in prev:
                    self.prime_pow.append(int(self.phi_val/n));
                    prev.append(n);

    def calc_phi(self):
        dict = self.pf_dict;prev = [];
        pf = dict.get_factors(self.grpSize);
        if pf == -1:
            self.phi_val = self.grpSize-1;
        elif pf != -2:
            phi_val = 1;
            for i in range(len(pf)):
                n = pf[i];
                if n not in prev:
                    phi_val = phi_val*((1-(1/n)));
                    prev.append(n);
            phi_val = self.grpSize*phi_val;
            self.phi_val = int(phi_val);
        print("\n\n");
        print("phi(",self.grpSize,") is: ",self.phi_val);

primitiveroots();
