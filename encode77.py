# -*- coding:utf-8 -*- 
    
def main():
    with open('idc.txt', 'r', encoding = 'utf-8') as fin:
        paper = fin.read()
    # length of search buffer and look-ahead buffer
    sb = 20
    lb = 20
    
    fout = open('enc77.txt', 'w', encoding = 'utf-8')
    pointer = 0
    length = len(paper)
    sw = '' # search buffer window
    
    while 1:
        # check if the pointer is near the end of the paper
        if pointer+len(sw)+lb < length:
            lw = paper[pointer+len(sw) : pointer+len(sw)+lb]
        else:
            lw = paper[pointer+len(sw) : ]  # look-ahead buffer window 

        matchLength = 0
        prefix = lw[0 : matchLength+1]
        p = sw.find(prefix)
        pos = len(sw)
        while (p != -1 and matchLength+1 < len(lw)):
            matchLength += 1
            prefix = lw[0 : matchLength+1]
            pos = p
            p = sw.find(prefix)
		# e.g., ababrar|rarrad <==> (3, 5, d) 
        if (matchLength and pos+matchLength == len(sw)):
            lpp = 0
            while (matchLength < len(lw)-1 and lw[lpp] == lw[matchLength]):
                lpp += 1
                matchLength += 1
        print(len(sw)-pos, matchLength, lw[matchLength], file = fout)
        
        sw = sw + lw[0 : matchLength+1]     
        cut = len(sw) - sb
        if cut > 0:
            sw = sw[cut:]
            pointer += cut
            if pointer+sb >= length:
                break       
    fout.close()

if __name__ == '__main__':
    main()
