from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
from flask.helpers import flash
from pymysql.connections import Connection
from requests.api import get
from wordbank import acak, getresult, angka, simbol, alphabet
import secrets
import random
from Univ_pass import gen_pass
import hashlib
from flask import session, app


@app.route("/")
def index():
    # current_data
    new_angka = acak(angka)
    new_simbol = acak(simbol)
    result1 = getresult(1)
    result2 = getresult(2)
    result3 = getresult(3)
    result4 = getresult(4)
    result5 = getresult(5)
    result6 = getresult(6)
    result7 = getresult(7)

    new_wordbank = ''
    new_result = ''

    if len(new_wordbank) <= 2:
        for char in range(0, 1):
            new_result += random.choice(result1)
            new_result += random.choice(result7)
            new_wordbank = new_result
    elif len(new_wordbank) <= 3:
        for char in range(0, 1):
            new_result += random.choice(result2)
            new_result += random.choice(result6)
            new_wordbank = new_result
    elif len(new_wordbank) <= 4:
        for char in range(0, 1):
            new_result += random.choice(result3)
            new_result += random.choice(result5)
            new_wordbank = new_result
    elif len(new_wordbank) <= 5:
        for char in range(0, 1):
            new_result += random.choice(result4)
            new_result += random.choice(result4)
            new_wordbank = new_result
    elif len(new_wordbank) <= 6:
        for char in range(0, 1):
            new_result += random.choice(result5)
            new_result += random.choice(result3)
            new_wordbank = new_result
    elif len(new_wordbank) <= 7:
        for char in range(0, 1):
            new_result += random.choice(result6)
            new_result += random.choice(result2)
            new_wordbank = new_result
    elif len(new_wordbank) <= 8:
        for char in range(0, 1):
            new_result += random.choice(result7)
            new_result += random.choice(result1)
            new_wordbank = new_result
    else:
        for char in range(0, 1):
            new_wordbank = new_result

    wordlist = new_wordbank
    while wordlist not in gen_pass.values:
        password = wordlist
        wordlist = password.join(secrets.choice(alphabet)
                                 for password in range(2))
        new_wordlist = wordlist.capitalize() + new_angka + new_simbol
        break

    securepass1 = wordlist[0].capitalize()
    securepass2 = wordlist[-1].lower()
    uniq = new_angka + new_simbol
    remember = new_wordbank
    generator = new_wordlist
    tabur = 'dx2'
    hashcode = hashlib.sha256(str(generator).encode('utf-8'))
    hash_digit = hashcode.hexdigest()
    uniq_hash = tabur + hash_digit
    return render_template('index.html', data=generator, data2=remember, data3=uniq, data4=securepass1, data5=securepass2, uniq_hash=uniq_hash)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
