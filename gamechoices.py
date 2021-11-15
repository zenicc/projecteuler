import time,random

peopleL = ["person 1", "person 2"]
actionL = ["easy action", "medium action", "hard action", "extreme action"]

personSelect = random.randint(0, 1)

print(peopleL[personSelect], "make ...      ", end="", flush=True)
time.sleep(1.5)
print(peopleL[personSelect - 1], "...      ", end="", flush=True)
time.sleep(1.5)
print("perform", random.choices(actionL, weights=(
    66, 25, 8, 1), k=1)[0])