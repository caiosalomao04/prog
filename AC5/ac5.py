import random

vidaM=random.randint(60,81)
vidaA=100
ataqueM=random.randint(20,31)
ataqueA=random.randint(10,21)
defesaA=random.randint(1,6)

def main(vidaM,vidaA,ataqueM,ataqueA,defesaA):
    print("Aventureiro: vida", vidaA,"- att",ataqueA,"-def",defesaA)
    print("Monstro: vida",vidaM,"- att",ataqueM)
    while vidaA and vidaM >0:
        if vidaM<=0:
            return "O monstro morreu!"
        vidaM - (random.randint(1,ataqueA))
        vidaA - (random.randint(1,ataqueM)-defesaA)
        if vidaA<=0:
            return "O aventureiro morreu!"
        print("Aventureiro: vida",vidaA,"- att",ataqueA,"-def",defesaA)
        print("Monstro: vida",vidaM,"- att",ataqueM)
        return

(main(vidaM,vidaA,ataqueM,ataqueA,defesaA))