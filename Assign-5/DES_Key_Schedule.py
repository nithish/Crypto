import sys;
class key_schedule:
    """docstring fs key_schedule."""
    def __init__(self):
        self.key = sys.argv[1];
        self.process_input();

    def process_input(self):
        if len(self.key) == 16:
            self.key = bin(int(self.key,16)).lstrip('0b');
            self.remove_parity();
            self.schedule();
        else:
            print("Key size is 64 bits or 16 hex digits");

    def schedule(self):
        i = 1;rounds = [1,2,9,16];
        self.split(self.skey);
        print("\n\n\nRound  # \t    ---------------56 bit Left shifted key------------------      " \
        "---------------48 bit PC-2 key------------------      HexDecimal Equivalent");
        while i <= 16:
            j = 1;
            while j < 3:
                c = self.lrotate(self.leftKey);
                d = self.lrotate(self.rightkey);
                self.leftKey = c;
                self.rightkey = d;
                if i in rounds:
                    break;
                j = j+1;
            key_56 = c+d;
            self.pc2(key_56,i);
            i = i+1;
        print("\n");

    def pc2(self,key_56,k):
        pc2_val = ["14", "17", "11", "24", "1", "5", "3", "28", "15", "6", "21", "10", "23", "19", "12", "4",
                    "26", "8", "16", "7", "27", "20", "13", "2", "41", "52", "31", "37", "47", "55", "30", "40", "51",
                    "45", "33", "48", "44", "49", "39", "56", "34", "53", "46", "42", "50", "36", "29", "32"];
        key_48 = [];
        for i in range(len(pc2_val)):
            key_48.insert(i,key_56[int(pc2_val[i])-1]);
        print("Round ",k,"\t-> ",key_56," -> ",''.join(key_48)," -> ", hex(int(''.join(key_48),2)).lstrip("0x"));

    def lrotate(Self,num):
        x = int(num,2);
        msb = x & (1 << 27);
        num = x << 1;
        if msb:
            num = num | 1;
        num = num & (2**28-1);
        num = (bin(num).lstrip('0b'));
        while len(num) < 28:
            num = '0'+num;
        return num;

    def split(self,key):
        self.leftKey = key[0:28];
        self.rightkey = key[28:];

    def remove_parity(self):
        i = 0;j = 1;
        self.skey = "";
        while i < 64:
            if j!=8:
                self.skey = self.skey + self.key[i];
                j = j+1;
            else:
                j = 1;
            i = i+1;

key_schedule();
