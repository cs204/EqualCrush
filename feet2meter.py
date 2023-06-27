def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    s1 = v.rstrip("ft")
    s = float(s1)
    s2 = s*3.28
    return s2

main()