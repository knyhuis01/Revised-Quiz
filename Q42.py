def hash_spam(complex):
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
                if total <= 4:
                    print("this tweet will be considered as a spam!")
