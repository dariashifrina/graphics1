#first assignment: test out image generating using ppms!

def crt_ppm(name, length, width, maxpix, content):
    header = "P3\n" + str(length) + " " + str(width) + "\n" + str(maxpix) + "\n"
    ppm_file=open(name +'.ppm','w')
    ppm_file.write(header + content)
    ppm_file.close()
    print " ... Done"

def ppm_content():
    content = ""
    for i in range(0,500):
        if(i%3 == 0):
            for m in range(0,500):
                content += "49 34 255 "
                m += 1
        elif(i%2 == 0):
            for x in range(0,500):
                content += "149 128 255 "
                x += 1
        else:
            for z in range(0,500):
                content += "255 77 228 "
                z += 1
        i += 1
    return content

crt_ppm("woo", 500, 500, 255, ppm_content())
