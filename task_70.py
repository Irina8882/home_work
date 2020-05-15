s = input ("Enter text: ")
abc = s[:3]
if "abc" in abc:
    s2 = s.replace("abc", "www")
    print (s2)
else:
    print (s + "zzz")
