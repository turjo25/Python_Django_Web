d = {}
while 1:
    k = input("Add name:")
    if(k == "stop"):
        break
    v = input("Add score:")
    d.update({
        k : v
    })
    for k,v in d.items():
        print(f"Name: {k} & score: {v}")
    
    