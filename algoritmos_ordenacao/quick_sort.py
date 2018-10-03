def quick_sort(lista, ini, fim):
	if ini < fim:
		pivot = partition(lista, ini, fim)
		quick_sort(lista, ini, pivot - 1)
		quick_sort(lista, pivot + 1, fim)


def partition(lista, ini, fim):
	pivot = lista[ini]
	cont = ini
	
	for i in range(ini + 1, fim + 1):
		if lista[i] < pivot:
			cont += 1
			lista[cont], lista[i] = lista[i], lista[cont]
				
	lista[ini], lista[cont] = lista[cont], lista[ini]

	return cont
