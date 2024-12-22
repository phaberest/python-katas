# Array Pair Sum Kata

## Problem Description
Create a function that finds all pairs of integers in an array that sum up to a target value.

### Requirements:
1. The function should take two parameters:
   - `numbers`: A list of integers
   - `target_sum`: The target sum to find
2. Return a list of tuples, where each tuple contains a pair of numbers that sum to the target
3. Each pair in the result should be sorted (smaller number first)
4. The list of pairs should be sorted
5. Implement proper input validation:
   - Input must be a list of integers
   - Target sum must be an integer
   - Raise ValueError for invalid inputs

### Examples:
```python
find_pairs([1, 2, 3, 4, 5], 7) # returns [(2, 5), (3, 4)]
find_pairs([1, 1, 2, 3], 4)    # returns [(1, 3), (1, 3)]
find_pairs([1, 2, 3], 10)      # returns [] (no pairs sum to 10)
```

## Getting Started
1. Your task is to implement the `find_pairs` function in `find_pairs.py`
2. Run the tests using: `python -m unittest test_find_pairs.py -v`
3. Make all tests pass!

## Learning Objectives
- Working with Python lists (arrays)
- Using sets for efficient lookups
- Handling edge cases
- Input validation
- Sorting and tuple manipulation

---

# Kata de Suma de Pares en Array

## Descripción del Problema
Crear una función que encuentre todos los pares de números enteros en un array que sumen un valor objetivo.

### Requisitos:
1. La función debe tomar dos parámetros:
   - `numbers`: Una lista de números enteros
   - `target_sum`: La suma objetivo a encontrar
2. Devolver una lista de tuplas, donde cada tupla contiene un par de números que suman el objetivo
3. Cada par en el resultado debe estar ordenado (número menor primero)
4. La lista de pares debe estar ordenada
5. Implementar una validación de entrada adecuada:
   - La entrada debe ser una lista de números enteros
   - La suma objetivo debe ser un número entero
   - Lanzar ValueError para entradas inválidas

### Ejemplos:
```python
find_pairs([1, 2, 3, 4, 5], 7) # devuelve [(2, 5), (3, 4)]
find_pairs([1, 1, 2, 3], 4)    # devuelve [(1, 3), (1, 3)]
find_pairs([1, 2, 3], 10)      # devuelve [] (ningún par suma 10)
```

## Cómo Empezar
1. Tu tarea es implementar la función `find_pairs` en `find_pairs.py`
2. Ejecuta las pruebas usando: `python -m unittest test_find_pairs.py -v`
3. ¡Haz que todas las pruebas pasen!

## Objetivos de Aprendizaje
- Trabajar con listas de Python (arrays)
- Usar conjuntos (sets) para búsquedas eficientes
- Manejar casos extremos
- Validación de entrada
- Manipulación de ordenamiento y tuplas

---

# Kata Somma di Coppie in Array

## Descrizione del Problema
Creare una funzione che trova tutte le coppie di numeri interi in un array la cui somma è uguale a un valore obiettivo.

### Requisiti:
1. La funzione deve accettare due parametri:
   - `numbers`: Una lista di numeri interi
   - `target_sum`: La somma obiettivo da trovare
2. Restituire una lista di tuple, dove ogni tupla contiene una coppia di numeri che sommati danno il valore obiettivo
3. Ogni coppia nel risultato deve essere ordinata (numero minore per primo)
4. La lista delle coppie deve essere ordinata
5. Implementare una corretta validazione degli input:
   - L'input deve essere una lista di numeri interi
   - La somma obiettivo deve essere un numero intero
   - Generare ValueError per input non validi

### Esempi:
```python
find_pairs([1, 2, 3, 4, 5], 7) # restituisce [(2, 5), (3, 4)]
find_pairs([1, 1, 2, 3], 4)    # restituisce [(1, 3), (1, 3)]
find_pairs([1, 2, 3], 10)      # restituisce [] (nessuna coppia somma a 10)
```

## Per Iniziare
1. Il tuo compito è implementare la funzione `find_pairs` in `find_pairs.py`
2. Esegui i test usando: `python -m unittest test_find_pairs.py -v`
3. Fai passare tutti i test!

## Obiettivi di Apprendimento
- Lavorare con le liste Python (array)
- Utilizzare i set per ricerche efficienti
- Gestire i casi limite
- Validazione degli input
- Manipolazione di ordinamento e tuple
