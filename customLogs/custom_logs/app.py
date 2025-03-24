from colorama import Fore

from custom_logs.base_log import connect_database
from custom_logs.decorators.time_decorator import log_time
from custom_logs.decorators.color_decorator import log_color
from custom_logs.decorators.file_decorator import log_to_file


# Aplicando vários decorators
@log_to_file("database_logs.txt")
@log_color(Fore.RED)
@log_time
def decorated_operation():
    return connect_database()


if __name__ == "__main__":
    decorated_operation()  # Executa a função com todos os decorators
