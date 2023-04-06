def even_number_of_evens(numbers):
    """
    Testing ideas:
    - Raise TypeError when not passed a list
    - if numbers empty return False
    - if no. of evens is odd, return False
    - if no. of evens is 0, return False
    - if no. of evens is even, return True
    """

    if isinstance(numbers, list):
        # pass criterion for returning 'False' on empty list
        if numbers == []:
            return False
        # Minimum code to pass check for list of even numbers
        else:
            # Set condition to say we have zero evens
            evens = 0
        
        # For each even number in the passed in list, increment the var
        # tracking the number of even numbers
        for n in numbers:
            if n % 2 == 0:
                evens += 1

        if evens:
            # Then check if the evens var is even and return True
            return evens % 2 == 0
        else:
            # Return 'False' if 'evens' var is falsy/0 (implied by above
            # if statement)
            return False
    else:
        raise TypeError("A list was not passed into the function")

    
    
    # return None


# if statement = 'Do this if the file is run directly'
if __name__ == "__main__":
    print(even_number_of_evens(5))