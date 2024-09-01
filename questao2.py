def verificarString(string):
    newString = string.lower()
    letraA = 'a' in newString
    quantidadeA = newString.count('a')

    if letraA:
        print (f"A letra 'a' aparece {quantidadeA} vezes na string")
    else:
        print ("A letra 'a' não aparece na string")
    
palavra = input('Digite uma palavra: ')
verificarString(palavra)