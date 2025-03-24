def log_time(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print(f"[{datetime.now()}] - Iniciando {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] - {func.__name__} finalizada!")
        return result

    return wrapper
