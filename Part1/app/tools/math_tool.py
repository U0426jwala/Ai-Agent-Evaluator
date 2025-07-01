from sympy import sympify, SympifyError

def calculate_expression(prompt: str) -> str:
    try:
        # Extract mathematical expression from prompt
        expr = prompt.lower().replace("calculate", "").strip()
        result = sympify(expr)
        return str(result.evalf())
    except SympifyError as e:
        raise ValueError(f"Invalid mathematical expression: {str(e)}")