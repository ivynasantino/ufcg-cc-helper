def replace_all(string, char_antes, char_depois):
	string_to_list(string)
	for i in range(0, len(string)):
		if string[i] == char_antes:
			string[i] = char_depois
	list_to_string(string)	


def replace_once(string, char_antes, char_depois):
	string_to_list(string)
	for i in range(0, len(string)):
		if string[i] == char_antes:
			string[i] = char_depois
			break
	list_to_string(string)


def my_count(string, char_procurado):
	contador = 0
	for i in range(0, len(string)):
		if string[i] == char_procurado:
			contador += 1
	return contador


def my_index(string, char_procurado):
	for i in range(0, len(string)):
		if string[i] == char_procurado:
			return i
		else:
			return 'SUBSTRING NOT FOUND'


def string_to_list(string):
	lista = []
	for i in range(0, len(string)):
		lista.append(string[i])
	string = lista


def list_to_string(lista):
	string = ''
	for i in range(0, len(lista)):
		string = string + lista[i]
	lista = string


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

def my_remove_all(lista, elemento):
    while i < len(lista):
        if lista[i] == elemento:
            lista.pop(i)
        else:
            i += 1
