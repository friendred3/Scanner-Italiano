import os 
def installazione():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install nmap')
    os.system('sudo apt-get install netdiscover')
    os.system('sudo pip3 install os')
print('INSTALLAZIONE DEI PACCHETTI...')
print('Sei sicuro di fare l\'installazione?\nPremere S/N.')
r = str(input('> '))

while(True):            
     if r == 's' or r == 'S':
        installazione()
        print('INSTALLAZIONE COMPLETATA')
        break
     elif r == 'n' or r == 'N':
        print('Installazione non effetuata')
        break
     else:
        print('Immettere S o N!')
        




        
            
