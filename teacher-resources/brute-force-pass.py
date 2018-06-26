import itertools
import string
import time;


def guess_password(real):
    starttime = time.time()*1000.0
    chars = string.ascii_lowercase + string.digits
    print(chars)
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                endtime = time.time()*1000.0
                duration = endtime - starttime
                return 'password is {}. found in {} guesses. Brute forcing took {} milliseconds.'.format(guess, attempts, duration)
            # print(guess, attempts)

print(guess_password('tes'))
