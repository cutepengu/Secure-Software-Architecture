def process_data(a, b):
    result = None
    try:
        print("Starting process")
        result = a / b  # Could raise ZeroDivisionError
        print("Process complete")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid input type")
    finally:
        print("Function execution finished")
    return result

print(process_data(10, 2))   # 5.0
print(process_data(10, 0))   # None, prints error message
print(process_data(10, 'a')) # None, prints type error