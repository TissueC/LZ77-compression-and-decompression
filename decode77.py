# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:58:42 2018

@author: Hao Sun
"""
def main():
    f = open("enc77.txt",'r',encoding="utf-8") 
    lines = f.readlines()
    cursor=-1
    out=''
    for i in range(0,len(lines)): 
        line=lines[i]
        tmplist=line.split()
        if(len(tmplist)==0):
            continue
        setoff=eval(tmplist[0])
        length=eval(tmplist[1])
        if(len(tmplist)==2): 
            #if the nest line is \n,the third element of the tuple is \n
            if(len(lines[i+1].split())==0):
                tail='\n'
            #else the third element of the tuple is ' '
            else:
                tail=' '
        else:
            tail=tmplist[2]
        if (setoff == 0 and length == 0):
                out += tail
                cursor+=1
        else:
                out += (out[(cursor-setoff+1):(cursor-setoff+length+1)] + tail)
                cursor+=length+1      
            # the repetition of dictionary
    fout = open('dec77.txt', 'w', encoding = 'utf-8')    
    print (out,file=fout)
    f.close()
    
main()
