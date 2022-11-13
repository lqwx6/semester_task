def error_handler(mode, cmplx_numbers):
    if len(cmplx_numbers) != 4: return True
    for number in cmplx_numbers:
        if not isinstance(number, int): return True
    
    if mode == 'div':
        if cmplx_numbers[2] + cmplx_numbers[3] == 0: return True
        
    return False


def get_numbers(cmplx_numbers):
    return complex(cmplx_numbers[0], cmplx_numbers[1]), complex(cmplx_numbers[2], cmplx_numbers[3])
    

def summa(cmplx_numbers):
    mode = 'sum'
    if error_handler(mode, cmplx_numbers): return 'error'
    a, b = get_numbers(cmplx_numbers)
    c = a + b
    return [c.real, c.imag]


def raznost(cmplx_numbers):
    mode = 'dif'
    if error_handler(mode, cmplx_numbers): return 'error'
    a, b = get_numbers(cmplx_numbers)
    c = a - b
    return [c.real, c.imag]


def multi(cmplx_numbers):
    mode = 'multi'
    if error_handler(mode, cmplx_numbers): return 'error'
    a, b = get_numbers(cmplx_numbers)
    c = a * b
    return [c.real, c.imag]


def divide(cmplx_numbers):
    mode = 'div'
    if error_handler(mode, cmplx_numbers): return 'error'
    a, b = get_numbers(cmplx_numbers)
    c = a / b
    return [float(f'{c.real:.4f}'), float(f'{c.imag:.4f}')]
    