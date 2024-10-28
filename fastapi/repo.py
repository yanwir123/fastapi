from model import ArithmeticRequest

class ArithmeticRepository:
    @staticmethod
    def calculate_if_else(request: ArithmeticRequest) -> dict:
        a, b, operation = request.a, request.b, request.operation
        response = {}

        if operation == "+":
            result = a + b
            response = {"code": 200, "mess": "succ", "data": f"{a} di tambah {b} adalah {result}"}
        elif operation == "-":
            result = a - b
            response = {"code": 200, "mess": "succ", "data": f"{a} di kurang {b} adalah {result}"}
        elif operation == "*":
            result = a * b
            response = {"code": 200, "mess": "succ", "data": f"{a} di kali {b} adalah {result}"}
        elif operation == "/":
            if b == 0:
                return {"code": 400, "mess": "error", "data": "Tidak bisa membagi dengan nol"}
            result = a / b
            response = {"code": 200, "mess": "succ", "data": f"{a} di bagi {b} adalah {result}"}
        else:
            response = {"code": 400, "mess": "error", "data": "Operasi tidak valid"}

        return response

    @staticmethod
    def calculate_switch(request: ArithmeticRequest) -> dict:
        a, b, operation = request.a, request.b, request.operation
        response = {}

        operations = {
            "+": lambda: a + b,
            "-": lambda: a - b,
            "*": lambda: a * b,
            "/": lambda: a / b if b != 0 else None
        }

        result = operations.get(operation)()

        if result is None:
            return {"code": 400, "mess": "error", "data": "Tidak bisa membagi dengan nol" if operation == "/" else "Operasi tidak valid"}

        response = {"code": 200, "mess": "succ", "data": f"{a} di {operation} {b} adalah {result}"}
        return response

    @staticmethod
    def calculate_ternary(request: ArithmeticRequest) -> dict:
        a, b, operation = request.a, request.b, request.operation
        response = {}

        result = (
            a + b if operation == "+" else
            a - b if operation == "-" else
            a * b if operation == "*" else
            a / b if operation == "/" and b != 0 else None
        )

        if result is None:
            return {"code": 400, "mess": "error", "data": "Tidak bisa membagi dengan nol" if operation == "/" else "Operasi tidak valid"}

        response = {"code": 200, "mess": "succ", "data": f"{a} di {operation} {b} adalah {result}"}
        return response
