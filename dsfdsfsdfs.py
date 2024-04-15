구구단 = int(input('"몇 단까지 출력할까요?"'))

for a in range(1,구구단+1) :
    print(f"-----,[",a,"단","],-----")
    for b in range(1,a+1) :
        print(a, "x" , b , "=", a*b)





