#first assignment: test out image generating using ppms!

def crt_ppm(name, length, width, maxpix, content):
    header = "P3\n" + str(length) + " " + str(width) + "\n" + str(maxpix) + "\n"
    ppm_file=open(name +'.ppm','w')
    ppm_file.write(header + content)
    ppm_file.close()
    print " ... Done"

def ppm_content():
    a = 233
    b = 201
    c = 255
    d = 255
    e = 179
    f = 232
    g = 163
    h = 86
    i = 89
    content = ""
    for i in range(0,500):
        if(i%3 == 0):
            for m in range(0,500):
                content += str(a%255) + " " + str(b%255) + " " + str(c%255) + " "
                a +=1
                b+=1
                c+=1
                m += 1
        elif(i%2 == 0):
            for x in range(0,500):
                content += str(d%255) + " " + str(e%255) + " " + str(f%255) + " "
                d +=1
                e +=1
                f +=1
                x += 1
        else:
            for z in range(0,500):
                content += str(f%255) + " " + str(g%255) + " " + str(h%255) + " "
                f +=1
                g +=1
                h +=1
                z += 1
        i += 1
    return content

crt_ppm("future_hair_color", 500, 500, 255, ppm_content())
