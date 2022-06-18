def plus():
    b = list()
    for i in range(3):
        val=input("请输入一个整数\n")
        try:
            val =int(val)
        except:
            print("haohaoshuru")
        if i < 5:
            a=val+i
        else:
            a=val

        b.append(a)
    print(b[0:-2])

plus()