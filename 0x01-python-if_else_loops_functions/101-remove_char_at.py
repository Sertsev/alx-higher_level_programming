def remove_char_at(str, n):
    c = ""
    for a in str:
        if n >= len(str) or n < 0:
            c = str
            break
        elif a == str[n]:
            continue
        else:
            c += a
    return c
