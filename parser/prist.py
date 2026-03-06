PRIST = []

with open("prist.txt", encoding="utf8") as file:
    PRIST = file.readlines()

PRIST = [x.strip().strip("-").lower() for x in PRIST]
