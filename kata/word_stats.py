def word_stats(text):
    """
    Analyze text and return statistics about word usage.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Dictionary containing:
            - 'frequencies': Dictionary of word frequencies (case-insensitive)
            - 'longest_word': The longest word(s) found (list if multiple)
            - 'avg_length': Average word length (float, rounded to 2 decimals)
        
    Example:
        word_stats("Hello hello WORLD") returns:
        {
            'frequencies': {'hello': 2, 'world': 1},
            'longest_word': ['hello', 'world'],
            'avg_length': 5.0
        }
        
    Tips:
    1. String methods that might be helpful:
       - split(): Splits string into words
       - strip(): Removes characters from start/end
       - lower(): Converts to lowercase
       
    2. Dictionary methods to consider:
       - dict.get(key, default): Get value or default if key missing
       - dict[key] = value: Set or update value
       
    3. For calculating longest words:
       - Use max() with len() to find longest length
       - Consider using set() to handle duplicates
       - Remember to sort the final list
       
    4. For average length:
       - Use round(number, decimals) to round to 2 places
       - Remember to handle division by zero case
       
    5. Input validation:
       - Check if input is a string using isinstance(text, str)
       - Handle empty or whitespace-only input
       
    6. Return structure:
       - Make sure to return a dictionary with all three required keys
       - Default values for empty input: {}, [], 0.0
    """
    # Your code here
    pass
