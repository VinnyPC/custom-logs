from colorama import Fore, Style


def log_color(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{color}[LOG] - Executando {func.__name__}...{Style.RESET_ALL}")
            return func(*args, **kwargs)

        return wrapper

    return decorator
