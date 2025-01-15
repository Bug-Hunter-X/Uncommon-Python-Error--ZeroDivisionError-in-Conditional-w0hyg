def function_with_uncommon_error(x):
    if x == 0:
        return float('inf') # Or handle it with a different value/exception
    else:
        return 1 / x