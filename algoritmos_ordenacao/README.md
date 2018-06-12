# Algoritmos de Ordenação
> Explicação dos principais algoritmos de ordenação

## Bubble Sort
O bubble sort irá executar bubble steps até a lista ser ordenada. Um bubble step é a comparação de elementos vizinhos de uma lista e sua troca se o primeiro elemento for maior que o segundo elemento.

##### Eficiencia do algoritmo
Algoritmo de ordem N^2.

##### Código em python

``` python
def bubble_step(alist):
    changed = False
    for i in range(len(alist)-1):
        if alist[i] > alist[i+1]:
            alist[i], alist[i+1] = alist[i+1], alist[i]
            changed = True
    return changed

def bubble_sort(alist):
    changed = True
    while changed:
        changed = bubble_step(alist)
```

## Insertion Sort
O insertion sort irá executar o insere ordenado para todos os itens da lista. O insere ordenado, insere um elemento numa lista ordenada de modo que a mantenha ordenada. O elemento é inserido na ultima posição da lista e é trocado até chegar a sua posição final. Isso ocorre através de uma comparação, se o elemento incluido for maior que o elemento que está atrás dele, eles trocam de posição, se não for a função irá parar e o elemento estará na posição dele.


##### Eficiência do algoritmo
Algoritmo de ordem n^2

##### Código em python

``` python
def ordered_insert(alist, i):
    for i in range(i, 0, -1):
        if alist[i] < alist[i-1]:
            alist[i], alist[i-1] = alist[i-1], alist[i]
        else:
            break

def insertion_sort(alist):
    for i in range(len(alist)):
        ordered_insert(alist, i)
```

## Selection sort
A partir da identificação do menor elemento da lista e o seu indice, o selection sort irá executar trocas de modo que o primeiro elemento da lista será trocado com o menor, o segundo elemento com o segundo menor e assim por diante até a lista ser ordenada.


##### Eficiência do algoritmo
Algoritmo de ordem n^2

##### Código em python

``` python
def select_smaller(alist, i):
    smaller = alist[i]
    index_smaller = i
    for c in range(i, len(alist)):
        if smaller > alist[c]:
            smaller = alist[c]
            index_smaller = c
    return index_smaller


def selection_sort(alist):
    for i in range(len(alist)):
        index_smaller = select_smaller(alist, i)
        alist[i], alist[index_smaller] = alist[index_smaller], alist[i]
```


