# qr.py

Uses Google Charts to generate QR codes

## Syntax

    
    usage: qr.py [-h] [-o OUTPUT] [-f FILE] [-s SIZE] [data]

    Make a QR code.

    positional arguments:
      data

    optional arguments:
      -h, --help                   show this help message and exit
      -o OUTPUT, --output OUTPUT   Output file prefix. Default 'qr'.
      -f FILE, --file FILE         Input file containing data
      -s SIZE, --size SIZE         Output file size in px. Must be between 100 and 512px. Default 320.


## Examples

### Generate from data on command line

    ./qr.py -o myqrcode 'Hello, world!'

Will generate `myqrcode_000.png` containing data 'Hello, world!'

### Generate from data in a file

    ./qr.py -o series -f mydata.dat

Will generate `series_000.png` through `series_xxx.png`, making one code for each line in the file
