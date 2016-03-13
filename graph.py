import sys, os

def writeLatex():

    os.system("rm /root/pro/pyth/graphing.tex")
    os.system("cp /root/pro/pyth/sample.tex /root/pro/pyth/graphing.tex")
    file = open("/root/pro/pyth/graphing.tex", 'r')
    array = []
    for line in file.readlines():
        array.append(line)

    file.close()

    file = open("/root/pro/pyth/graphing.tex", 'w')
    for i in array:
        if i.find("\\addplot"):
            file.write(i)

        else:
            try:
                string = "\\addplot[blue]{" + sys.argv[1] + "};\n"
                file.write(string)
            except IndexError:
                string ="\\addplot[blue]{x^2};\n"
                file.write(string)




    file.close()


def runLatex():

    os.system("pdflatex /root/pro/pyth/graphing.tex")
    os.system("evince /root/pro/pyth/graphing.pdf")

def main():
    writeLatex()
    runLatex()


if __name__=="__main__":
    main()
