with open('/home/kamilo/Projects/practice-python-course/day-1/1_listowanie_plikow_w_katalogu/main.py', 'r') as f:
    counter = 0

    for line in f.readlines():
        stripped_line = line.strip()
        
        if any(c in stripped_line for c in ("\n", "\r")) or stripped_line.startswith("#") or stripped_line == "":
            continue
        
        counter += 1

    print(f"loc: {counter}")
