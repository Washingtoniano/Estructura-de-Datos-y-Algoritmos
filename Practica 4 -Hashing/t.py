import random
def comprobacion(clave):
    band=False
    con=1
    print("Clave",clave)
    i=2
    while i<clave and con==1:
        r=clave%i
        if r==0 and i!=clave:
            con+=1
        i+=1
    if con==1:
        band=True
    #print("r:",r)
        
    return band
    
def primo(clave):
        r=clave
        if not comprobacion(clave):
            #n=0
            #clave=str(clave)
            #lon=len(clave)
            #for i in range(lon):
            #    n+=int(clave[i])
            band=False
            print("prim:",r)
            while band==False:
                r+=1
                print("prim:",r)
                if(comprobacion(r)):
                    band=True
                    #r=n
                #else:
                #    n+=1

        print("Numero primo:",r)
if __name__ =="__main__":
    n=10
    cont=0
    while cont<n:
        d=random.randint(000,100)
        primo(d)
        print("Cont:",cont)
        cont+=1
    print("//////")
            