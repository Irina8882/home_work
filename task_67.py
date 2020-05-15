import re
text = "You can learn python, or you can eat a sausage sandwich and play in a Sony playstation"
m = re.findall (r'\b[s]\w+', text)
print (m)