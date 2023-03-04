from pathlib import Path

l = Path("skills")

for i in l.iterdir():
    s = f"<img src='skills/{i.name}' style='width:45px'>"
    print(s)