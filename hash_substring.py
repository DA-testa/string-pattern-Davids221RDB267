# python3

def read_input():
   
    ievadits = input()
    if "I" in ievadits:
        
        pattern=input()
        text=input()
        
    else:
        testi="tests/06"
        with open(testi,"r") as t:
            
            pattern=t.readline()
            text=t.readline()
   
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
        
        if txt-pat>a:
             txthash=hash(text[a+1:pat+a+1])
                 
    return get


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

