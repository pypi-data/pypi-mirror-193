def execute_handcalcs(function, *args, **kwargs) -> tuple[str, dict]:
    """Executes the given function through handcalcs and returns the raw latex str
    and values dict
    """
    latex, values = function(*args, **kwargs)
    latex = (
        latex
        .replace(r'\begin{aligned}', '')
        .replace(r'\end{aligned}', '')
        .strip()
        )
    return latex, values