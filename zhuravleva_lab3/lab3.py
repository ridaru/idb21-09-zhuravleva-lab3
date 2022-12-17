import re
import codecs
find = []
with open("test.html", "r", encoding='utf-8') as f:
    for i in f:
        file = f.readline()
        found = re.findall(r'http[\S][^}{]*?[.]+.*?(?=")',file) #http+непробельные символы[исключая {}] - 0 или более вхождений(лениво), [.] - включая точку - одно или более вхождение, 0 или более вхождений любых символов(лениво), конец искомой подстроки - "
        if len(found) != 0:
            for i in range(len(found)):
                find.append(found[i])
print(find)