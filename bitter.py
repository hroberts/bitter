#!/usr/local/bin/python3

from flask import Flask, render_template, request, flash

import math

app = Flask(__name__)

def decimal_to_binary( decimal ):
    decimal = int( decimal )

    bits_length = math.floor( math.log( decimal, 2 ) ) + 1
    bits = [ '0' for x in range( bits_length ) ]

    while ( decimal > 0 ):
        print( "decimal: " + str( decimal ) )
        digit = math.floor( math.log( decimal, 2 ) )
        print( "digit: " + str( digit ) )
        bits[ bits_length - digit - 1 ] = "1"
        decimal -= 2 ** digit

    return ''.join( bits );

@app.route("/" )
def bitter():
    message = ''

    try:
        bits_in = request.args.get( 'bits', '' )
        decimal_in = request.args.get( 'decimal', '' )

        bits_out = decimal_to_binary( decimal_in ) if decimal_in else ''
        decimal_out = int( bits_in, 2 ) if bits_in else ''

        return render_template( 'bitter.html',
            decimal_in = decimal_in,
            decimal_out = decimal_out,
            bits_in = bits_in,
            bits_out = bits_out )

    except ValueError:
        message = "Input error - numbers must be in decimal or binary form"
        return render_template( 'bitter.html', message = message )


if __name__ == "__main__":
    app.run()
