# my cringy neovim couldn't handle thai-
# characters (cries)

def str2hms(hms_str):
 t = hms_str.split(':')
 return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
 return ('0'+str(h))[-2:] + ':' + \
 ('0'+str(m))[-2:] + ':' + \
 ('0'+str(s))[-2:]

def to_sec(h,m,s):
 return (h*60 + m)*60 + s

def to_hms(s):
 ret_s = s % 60
 s = int(s/60)
 ret_m = s % 60
 s = int(s/60)
 ret_h = s
 return ret_h, ret_m, ret_s

def diff(h1,m1,s1,h2,m2,s2):
 t1 = to_sec(h1, m1, s1);
 t2 = to_sec(h2, m2, s2);
 dt = t2-t1
 if (dt < 0):
  dt += 86400
 return to_hms(dt)

def main():
 h1, m1, s1 = str2hms(input())
 h2, m2, s2 = str2hms(input())
 dh, dm, ds = diff(h1, m1, s1, h2, m2, s2)
 print(hms2str(dh, dm, ds))

exec(input()) # DON'T remove this line