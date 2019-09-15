#! python3

import sys  # [app, arg1...arginfinity]
import webbrowser

address = 'Paypal'

# check if args are passed
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])

webbrowser.open('http://www.google.com/maps/place/' + address)
