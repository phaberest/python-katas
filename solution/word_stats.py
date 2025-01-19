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
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    if not text.strip():
        return {
            'frequencies': {},
            'longest_word': [],
            'avg_length': 0.0
        }
    
    # Split text into words and clean them
    words = [word.strip('.,!?()[]{}":;').lower() 
            for word in text.split()
            if word.strip('.,!?()[]{}":;')]
    
    # Calculate frequencies
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    
    # Find longest word(s)
    if words:
        max_length = max(len(word) for word in words)
        # Use set to get unique words, then sort them
        longest_words = sorted(set(word for word in words if len(word) == max_length))
    else:
        longest_words = []
    
    # Calculate average length
    avg_length = round(sum(len(word) for word in words) / len(words), 2) if words else 0.0
    
    return {
        'frequencies': frequencies,
        'longest_word': longest_words,
        'avg_length': avg_length
    }
