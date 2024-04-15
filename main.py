import os
import time

def main():
    Nbtype = 0 # 0: undefined, 1: int, 2: float, 3: error
    inputNB = input("Say a number : ")
    
    try:
        inputNB = int(inputNB)
        Nbtype = 1
    except ValueError:
        try: 
            inputNB = float(inputNB)
            Nbtype = 2
        except ValueError:
            if inputNB.lower() in ["exit", "end"]:
                print("\nEnd of the program!")
                exit()
            else:
                os.system('cls')
                print(f"Error: {inputNB} isn't a number.")
                Nbtype = 3
                main()

    unit_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens_list = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_list = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    other_list = ["hundred", "", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
    point = "point"
    
    listglobalresult = []
    inputNB = str(inputNB)
    integer_part, *decimal_part = inputNB.split(".")  # Splitting integer and decimal parts

    NBlist = list(integer_part)
    ReverseNBlist = NBlist[::-1]
    
    NBloop = 0
    for i in [ReverseNBlist[i:i+3] for i in range(0, len(ReverseNBlist), 3)]:
        i = i[::-1]
        listlocalresult = []
        
        if len(i)==3:
            if i[1] == "1":
                strlocalresult = unit_list[int(i[0])] + " " + other_list[0] + " " + teens_list[int(i[1])+1]
            else:
                strlocalresult = unit_list[int(i[0])] + " " + other_list[0] + " " + tens_list[int(i[1])-1] + " " + unit_list[int(i[2])]
        if len(i)==2:
            if i[0] == "1":
                strlocalresult = teens_list[int(i[1])-1]
            else:
                strlocalresult = tens_list[int(i[0])-1] + " " + unit_list[int(i[1])]

        listlocalresult = strlocalresult.split(" ")
        if "zero" in listlocalresult:
            listlocalresult.remove("zero")
        listlocalresult.append(other_list[NBloop+1])
        NBloop += 1
                
        listglobalresult.append(" ".join(listlocalresult))
    listglobalresult = listglobalresult[::-1]
    strglobalresult = " ".join(listglobalresult)
    
    if decimal_part:
        strglobalresult += " " + point + " " + " ".join([unit_list[int(d)] for d in decimal_part[0]])

    print(strglobalresult)

if __name__ == "__main__":
    os.system('cls')
    main()