#!/usr/bin/env python

from api import create_app
app = create_app()

if __name__ == '__main__':
    # ./run.py must be the only way to get here.
    # debug in production gets you hacked.
    app.run(debug=True)
