print("Witam w Algorytmie Flagi Francji! \n")

def flaga(lista, zliczanie):          
    n,s = 0, 0
    w = zliczanie - 1              
  
    while s <= w:        
        if lista[s] == 0:     
            lista[n], lista[s] = lista[s], lista[n]   
            n += 1          
            s += 1
        elif lista[s] == 1:   
            s += 1         
        else:                 
            lista[s], lista[w] = lista[w], lista[s] 
            w = w - 1   
    return lista


lista = [0,2,1,2,2,1,0]
print("To jest lista przed sortowaniem: ", lista)
zliczanie = len(lista)
lista = flaga(lista, zliczanie)
print("To jest posortowana lista: ", lista)

"""

Opis Programu:

W programie najpierw definiowana jest funkcja o nazwie flaga. Funkcja ta przyjmuje dwa argumenty: listę do posortowania oraz liczbę elementów w tej liście.

Następnie w ciele funkcji definiowane są zmienne n, s i w, które odpowiadają za pozycje elementów w liście.
Zmienna s jest inicjalizowana jako 0, co oznacza początek listy, natomiast zmienna w inicjalizowana jest jako zliczanie - 1, co oznacza koniec listy.
Zmienna n jest inicjalizowana jako 0, ale będzie inkrementowana w trakcie sortowania.

Następnie funkcja wchodzi w pętlę while, która będzie wykonywana dopóki zmienna s będzie mniejsza lub równa zmiennej w.
W pętli while sprawdzane są kolejne elementy listy.
Jeśli element jest równy 0, to zamieniany jest z elementem o pozycji n i zmienna n jest inkrementowana.
Jeśli element jest równy 1, to zmienna s jest inkrementowana.
Jeśli element jest równy 2, to zamieniany jest z elementem o pozycji w i zmienna w jest dekrementowana.

Na końcu funkcja zwraca posortowaną listę.

W głównym ciele programu definiowana jest lista zawierająca elementy, które mają zostać posortowane. Następnie wyświetlana jest ta lista. Po tym następuje wywołanie funkcji "flaga", która sortuje listę. Na końcu program wyświetla już posortowaną listę.

"""

