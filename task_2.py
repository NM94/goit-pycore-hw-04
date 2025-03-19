def get_cats_info(path):
    keys = ["id","name","age"]
    cats_list = []
    try:
     with open(path, "r", encoding="utf-8") as file:
        for line in file:
            lines = line.strip().split(",")
            for i in range(len(lines)):
                dictionery = {}
                dictionery[keys[i]] = lines[i]
                cats_list.append(dictionery)
    except Exception as e:
        print(f"Помилка {e}")  
        return None      
    return cats_list       

            
with open("cats_file.txt", "w", encoding="utf-8") as cats:
    cats.write('60b90c1c13067a15887e1ae1,Tayson,3'
    '\n60b90c2413067a15887e1ae2,Vika,1'
    '\n60b90c2e13067a15887e1ae3,Barsik,2'
    '\n60b90c3b13067a15887e1ae4,Simon,12'
    '\n60b90c4613067a15887e1ae5,Tessi,5')
    

cats_info = get_cats_info("cats_file.txt")
print(cats_info)