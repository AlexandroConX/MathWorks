import sys

def hanoi(discos,origen,temporal,destino):
    if discos==1:
        print("Mueve de poste",origen, "a", destino)
    else:
        hanoi(discos-1,origen,destino,temporal)
        print("Mueve de poste",origen, "a", destino)
        hanoi(discos-1,temporal,origen,destino)
hanoi(int(sys.argv[1]),"A","B","C")
      
