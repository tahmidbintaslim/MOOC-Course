from numbthy import *

p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171

g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568

h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

#p = 1073676287
#g=1010343267
#h=857348958
#B = 2**10

B = 2**20
gb = powmod(g, B, p)

def modinv(a, m):
    gcd, x, y = xgcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


m = dict()

print "BEGIN BUILD TABLE"

for i in range(1, 2**20):
    tmp = powmod(g, i, p)
    tmpi = modinv(tmp, p)
    m[ (h*tmpi) % p] = i

print "BUILD TABLE FINISH"

for i in range(1, 2**20):
    tmp = powmod(gb, i, p)
    if tmp in m:
        print B*i+m[tmp]
        print i
        break;


print "RUN FINISH"