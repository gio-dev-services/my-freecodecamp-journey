def square_root_bisection(number, tolerance=1e-7, iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number in (0, 1):
        print(f"The square root of {number} is {number}")
        return number
    
    low_num = 0
    high_num = max(1, number)
    num_iterations = 0

    while high_num - low_num > tolerance and num_iterations < iterations:
        mid = (low_num + high_num) / 2
        if mid * mid < number:
            low_num = mid
        else:
            high_num = mid
        num_iterations += 1
    
    if high_num - low_num <= tolerance:
        root = (low_num + high_num) / 2
        print(f"The square root of {number} is approximately {root}")
        return root
    print(f"Failed to converge within {iterations} iterations")
    return None

    
