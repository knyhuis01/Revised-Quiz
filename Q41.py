def count_hastag(complex):
    total = 0
    index = 0
    character = "\#"
    while index < len(complex):
        for ch in complex:
            if ch == character:
                total += 1
                index +=1
            else:
                index +=1
    return total
count_hastag("\#peaceout#wow")
