def error_handler(mode, cmplx_numbers):
    if len(cmplx_numbers) != 4: return True
    for number in cmplx_numbers:
        if not isinstance(number, int): return True

    if mode == 'div':
        if cmplx_numbers[2] + cmplx_numbers[3] == 0: return True

    return False


def summa(cmplx_numbers):
    mode = 'sum'
    have_errors = error_handler(mode, cmplx_numbers)
    if have_errors: return 'error'
    return ([cmplx_numbers[0] + cmplx_numbers[2], cmplx_numbers[1] + cmplx_numbers[3]])

def raznost(cmplx_numbers):
    mode = 'dif'
    have_errors = error_handler(mode, cmplx_numbers)
    if have_errors: return 'error'
    return ([cmplx_numbers[0] - cmplx_numbers[2], cmplx_numbers[1] - cmplx_numbers[3]])

def multi(cmplx_numbers):
    mode = 'multi'
    have_errors = error_handler(mode, cmplx_numbers)
    if have_errors: return 'error'
    return ([float(cmplx_numbers[0] * cmplx_numbers[2] - cmplx_numbers[1] * cmplx_numbers[3]), float(cmplx_numbers[0] * cmplx_numbers[3] + cmplx_numbers[1] * cmplx_numbers[2])])

def divide(cmplx_numbers):
    mode = 'div'
    have_errors = error_handler(mode, cmplx_numbers)
    if have_errors: return 'error'
    return ([ float('{:.4f}'.format((cmplx_numbers[0] * cmplx_numbers[2] + cmplx_numbers[1] * cmplx_numbers[3]) / (cmplx_numbers[2] ** 2 + cmplx_numbers[3] ** 2))), float('{:.4f}'.format( (cmplx_numbers[2] * cmplx_numbers[1] - cmplx_numbers[0] * cmplx_numbers[3]) / (cmplx_numbers[2] ** 2 + cmplx_numbers[3] ** 2) )) ])