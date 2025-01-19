# Word Statistics Kata

## Problem Description
Create a function that analyzes text and returns various statistics about word usage using dictionaries.

### Requirements:
1. The function should take a string input and return a dictionary with three keys:
   - `frequencies`: Dictionary of word frequencies (case-insensitive)
   - `longest_word`: List of the longest word(s) found
   - `avg_length`: Average word length as float (rounded to 2 decimals)
2. Implement proper text processing:
   - Remove punctuation from words
   - Convert all words to lowercase
   - Skip empty strings
3. Handle edge cases:
   - Empty or whitespace-only input should return appropriate default values
   - Invalid input should raise ValueError

### Examples:
```python
word_stats("Hello hello WORLD") 
# Returns:
{
    'frequencies': {'hello': 2, 'world': 1},
    'longest_word': ['hello', 'world'],
    'avg_length': 5.0
}

word_stats("The quick brown fox")
# Returns:
{
    'frequencies': {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1},
    'longest_word': ['brown', 'quick'],  # Both 5 letters
    'avg_length': 4.0
}
```

## Getting Started
1. Your task is to implement the `word_stats` function in `word_stats.py`
2. Run the tests using: `python -m unittest test_word_stats.py -v`
3. Make all tests pass!

## Learning Objectives
- Working with Python dictionaries
- String manipulation and text processing
- Handling edge cases
- Using dictionary methods (get, update)
- List comprehension and filtering

---

# Kata de Estadísticas de Palabras

## Descripción del Problema
Crear una función que analice texto y devuelva varias estadísticas sobre el uso de palabras utilizando diccionarios.

### Requisitos:
1. La función debe tomar una cadena de texto como entrada y devolver un diccionario con tres claves:
   - `frequencies`: Diccionario de frecuencias de palabras (sin distinción entre mayúsculas y minúsculas)
   - `longest_word`: Lista de la(s) palabra(s) más larga(s)
   - `avg_length`: Longitud promedio de palabras como float (redondeado a 2 decimales)
2. Implementar procesamiento de texto adecuado:
   - Eliminar puntuación de las palabras
   - Convertir todas las palabras a minúsculas
   - Omitir cadenas vacías
3. Manejar casos especiales:
   - Entrada vacía o solo espacios debe devolver valores predeterminados apropiados
   - Entrada inválida debe lanzar ValueError

### Ejemplos:
```python
word_stats("Hello hello WORLD")
# Devuelve:
{
    'frequencies': {'hello': 2, 'world': 1},
    'longest_word': ['hello', 'world'],
    'avg_length': 5.0
}

word_stats("The quick brown fox")
# Devuelve:
{
    'frequencies': {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1},
    'longest_word': ['brown', 'quick'],  # Ambas de 5 letras
    'avg_length': 4.0
}
```

## Cómo Empezar
1. Tu tarea es implementar la función `word_stats` en `word_stats.py`
2. Ejecuta las pruebas usando: `python -m unittest test_word_stats.py -v`
3. ¡Haz que todas las pruebas pasen!

## Objetivos de Aprendizaje
- Trabajar con diccionarios de Python
- Manipulación de cadenas y procesamiento de texto
- Manejo de casos especiales
- Usar métodos de diccionarios (get, update)
- Comprensión de listas y filtrado

---

# Kata Statistiche delle Parole

## Descrizione del Problema
Creare una funzione che analizza il testo e restituisce varie statistiche sull'uso delle parole utilizzando i dizionari.

### Requisiti:
1. La funzione deve accettare una stringa come input e restituire un dizionario con tre chiavi:
   - `frequencies`: Dizionario delle frequenze delle parole (senza distinzione tra maiuscole e minuscole)
   - `longest_word`: Lista della/e parola/e più lunga/e
   - `avg_length`: Lunghezza media delle parole come float (arrotondata a 2 decimali)
2. Implementare un corretto processamento del testo:
   - Rimuovere la punteggiatura dalle parole
   - Convertire tutte le parole in minuscolo
   - Saltare le stringhe vuote
3. Gestire i casi limite:
   - Input vuoto o solo spazi deve restituire valori predefiniti appropriati
   - Input non valido deve generare ValueError

### Esempi:
```python
word_stats("Hello hello WORLD")
# Restituisce:
{
    'frequencies': {'hello': 2, 'world': 1},
    'longest_word': ['hello', 'world'],
    'avg_length': 5.0
}

word_stats("The quick brown fox")
# Restituisce:
{
    'frequencies': {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1},
    'longest_word': ['brown', 'quick'],  # Entrambe di 5 lettere
    'avg_length': 4.0
}
```

## Per Iniziare
1. Il tuo compito è implementare la funzione `word_stats` in `word_stats.py`
2. Esegui i test usando: `python -m unittest test_word_stats.py -v`
3. Fai passare tutti i test!

## Obiettivi di Apprendimento
- Lavorare con i dizionari Python
- Manipolazione delle stringhe e processamento del testo
- Gestione dei casi limite
- Utilizzare i metodi dei dizionari (get, update)
- List comprehension e filtraggio
