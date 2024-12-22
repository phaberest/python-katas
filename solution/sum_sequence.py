def sum_sequence(n):
    """
    Calculate the sum of numbers from 1 to n using a for loop.
    
    Args:
        n (int): A positive integer
        
    Returns:
        int: The sum of all integers from 1 to n
        
    Example:
        sum_sequence(3) returns 6 (1 + 2 + 3)
        sum_sequence(5) returns 15 (1 + 2 + 3 + 4 + 5)
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
        
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
