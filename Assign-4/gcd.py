class GCD:
    """Calculates GCD of two numbers"""
    def _gcd(self,a,b):
        if(b == 0):
            return a;
        else:
            return self._gcd(b,a%b);
