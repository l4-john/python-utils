
fr = open("rPad.txt", "r", encoding="utf-8");
text = "";
while True:
    line = fr.readline();
    if not line : break;
    text += line.rstrip() + "\n";
fr.close();

print(text);
fw = open("rPad.txt", "w", encoding="utf-8");
fw.write(text);
fw.close();
