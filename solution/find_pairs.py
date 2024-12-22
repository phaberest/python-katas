def find_pairs(numbers, target_sum):
    """
    Find all pairs of numbers in the array that sum up to the target value.
    
    Args:
        numbers (list): List of integers
        target_sum (int): Target sum to find
        
    Returns:
        list: List of tuples containing pairs of numbers that sum to target_sum
        
    Example:
        find_pairs([1, 2, 3, 4, 5], 7) returns [(2, 5), (3, 4)]
        find_pairs([1, 1, 2, 3], 4) returns [(1, 3), (1, 3)]
    """
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")
    if not isinstance(target_sum, int):
        raise ValueError("Target sum must be an integer")
        
    pairs = []
    seen = set()
    
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs.append((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return sorted(pairs)
