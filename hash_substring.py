# python3

def read_input():
   
    ievadits = input()
    if "I" in ievadits:
        text=input()
        pattern=input()
        
    else:
        testi="tests/06"
        with open(testi,"r") as t:
            text=t.readline()
            pattern=t.readline()
   
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    get=[]
    txt=len(text)
    pat=len(pattern)

    txthash=hash(text[:pat])
    pathash=hash(pattern)
                 
                 
    for a in range(txt-pat+1):    
        if pattern==text[a:pat+a] and txthash==pathash:
           get.append(a)
        
        if a<txt-pat:
             txthash=hash(txt[1+a:pat+a+1])
                 
    return get


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

