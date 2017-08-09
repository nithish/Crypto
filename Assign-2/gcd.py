class GCD:
    """Calculates GCD of two numbers"""
    def _gcd(self,a,b):
        if(b == 0):
            print(a);
        else:
            print(a," ",b);
            self._gcd(b,a%b);
a = GCD();
a._gcd(5,7);
