def my_replace(lista_string, char_antes, char_depois):
    if type(lista_string) == str:
        list(lista_string)

    for i in range(len(lista_string)):
        if lista_string[i] == char_before:
            lista_string[i] = char_after



def my_filter(lista, elemento):
    while i < len(lista):
        if lista[i] == elemento:
            lista.pop(i)
        else:
            i += 1


def my_count(string_lista, elemento):
	counter = 0
	for e in string_lista
		if e == elemento:
			counter += 1
	return counter


def my_index(string_lista, elemento):
	for i in range(0, len(string_lista)):
		if string[i] == elemento:
			return i
	
        return -1


def my_in(lista, elemento):
    for e in lista:
        if e == elemento:
            return True
    return False


def my_slice(eh_lista, str_list, comeco, fim):
    if eh_lista:
        lista_aux = []
        for i in range(comeco, fim):
            lista_aux.append(str_list[i])
    else:
        str_aux = ''
        for i in range(comeco, fim):
            str_aux += str_list[i]


def my_remove(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista.pop(i)
            break

