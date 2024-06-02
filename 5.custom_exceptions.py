class CustomError(Exception):
    def __init__(self, message):
        self.message = message

def risky_operation():
    raise CustomError("Something went wrong in the risky operation.")

try:
    risky_operation()
except CustomError as e:
    print(f"CustomError: {e.message}")
