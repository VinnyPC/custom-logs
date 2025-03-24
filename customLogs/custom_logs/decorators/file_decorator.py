def log_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as file:
                file.write(f"{func.__name__} retornou: {result}\n")
            return result

        return wrapper

    return decorator
