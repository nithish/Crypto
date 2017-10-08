from math import sqrt;
class primefactors:
    """Returns the array of prime factors if given numb is composite else '-1',
        meaning that the given number is prime"""
    def __init__(self):
        pf_dict = {};
        with open('C-10000.txt') as f:
            for line in f:
                str = line.split('=');
                pf_dict[int(str[0])] = [int(x) for x in str[1].split('*')];
        self.pf_dict = pf_dict;

    def get_factors(self,num):
        if num > 11374:
            return -2;
        elif num in self.pf_dict:
            return self.pf_dict[num];
        else:
            return -1;
