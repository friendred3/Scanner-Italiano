import os
##logo
os.system('clear')
def logo():
    print( """
     _________  ________       __
    |   ______]|   __   \     |  |
    |   |      |  |__|  |     |  |
    |   |__    |  __  __/     |  |
    |   ___]   |  |\  \       |  |
    |  |       |  | \  \      |__|
    |  |       |  |  \  \      __
    |__|       |__|   \__\    (__)

    """)
##indice
def logo1():
    print("""
    Questo tool ti permette di scannerezzare gli ip pubblici o locali con NMAP.
    Ti permette di trovare gli ip in una rete locale con NETDISCOVER.                     
    Se vorresti usare qualche funzione in più, ho aggiunto anche ZENMAP.    
    """)
##menù
def menu():
    print("""
      1) Scanner per IP pubblico
      2) Scanner per IP locale
      3) Trovare gli IP della rete locale [ netdiscover ]
      4) Zenmap  
      """)


while(True):
    logo()
    logo1()
    menu()
    ##errore numero intero
    try:    
        opzione = int(input('Enter numeber: '))
        break
    except ValueError:
        os.system('clear')
        print('NON È UN INTERO')      
##scanner dell'ip pubblico con nmap
if opzione == 1:
    print('Scrivi qua l\'IP pubblico:')
    ipp = str(input())
    os.system('sudo nmap '+ ipp +' try -Pn')
##scanner dell'ip locale con nmap   
elif opzione == 2:
    print('Scrivi qua l\'IP locale:')
    ipl = str(input())
    os.system('sudo nmap -sS -sV '+ ipl )
##trovare gli ip nella rete locale    
elif opzione == 3:
    print('Netdiscover')
    os.system('sudo netdiscover')
##apertura di zenmap
elif opzione == 4:
    print('Zenmap')
    os.system('sudo zenmap')
##errore del menù        
else:
    print('NON È SUL MENÙ')
        
