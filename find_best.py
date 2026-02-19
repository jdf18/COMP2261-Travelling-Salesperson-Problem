from pathlib import Path

files = Path("output").rglob("Alg*.txt")

best = {}

for file in files:
    with open(file) as f:
        parts = f.read().split(",")

    alg = file.name[3]
    num = file.name[22:25]
    length = int(parts[4].split("=")[1].strip())

    if not alg in best.keys():
        best.update({alg:{}})

    if not num in best[alg].keys():
        best[alg].update({num:(file, length)})
        continue

    if length < best[alg][num][1]:
        best[alg][num] = (file, length)


store = Path("final_results")
if not store.exists():
    store.mkdir()

for alg, r in best.items():
    for num, v in r.items():
        file, _ = v
        dest = store/Path(f"Alg{alg}_AISearchfile{num}.txt")
        dest.write_text(file.read_text())

print(best)


