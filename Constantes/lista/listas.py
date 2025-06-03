numeros = [1, 2, 3, 4, 5]
nomes = ["Maria" , "Joaquin" , "Eduardo"]

def mostrar_linhas():
    print('-' * 30)
    
mostrar_linhas()

print(nomes[0]) # Maria
print(nomes[1])
print(nomes[2])

mostrar_linhas()

nomes[0] = "João" #estava Maria

print(nomes[0]) # alterado para Maria
print(nomes[1])
print(nomes[2])

mostrar_linhas()

nomes.append('João')# append adiciona nomes no final.
nomes.append('Joana')

print(nomes[0]) 
print(nomes[1])
print(nomes[2])
print(nomes[3])# acresentando o João
print(nomes[4])# acresentando a Joana

print(nomes)

mostrar_linhas()

nomes.insert(1, "Fernando")# insere "Fernando" na posição 1
print("Após insert:", nomes)

mostrar_linhas()

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no índice 2
print("Após modificando:", nomes)

mostrar_linhas()

#removendo elelmentos
del nomes[3]# Remove o elemento no índice 3
print("Após del", nomes)

mostrar_linhas()

nomes.remove("Joana") # Remove a primeira ocorrência de "Joana"
print("Após remove", nomes)

mostrar_linhas()

removido = nomes.pop(2) #remove e retorna o elemento no índice 2
print(f"Após pop (removido'{removido}')", nomes)

mostrar_linhas()

nomes.clear() # Esvaziar a lista
print("Após clear:", nomes)