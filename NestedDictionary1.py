import random as rand

d = {}
names = ["ramu", "raghav", "raja", "bheem"]

for i in range(1,10):
    d[f"student_{i}"] = {
    "name": names[rand.randint(0, len(names) - 1)],
    "score": rand.randint(70, 100)
    }

max_student = None
max_score = -1

for sid, info in d.items():
    if info["score"] > max_score:
        max_score = info["score"]
        max_student = sid

print(d)

print("--------------------------------------")
print("max student:", max_student, d[max_student])