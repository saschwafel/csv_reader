# csv_reader
Module to read and write CSVs using the Python CSV library

# =================================
I got tired of writing a CSV function in every script I was working on, so I wrote a Python module that is portable and can be imported into anything. It’s attached here. 

To use: 

Import the module via 

    import csv_reader

or 

    from csv_reader import open_csv, write_csv # (you’ll need to copy it into the working directory)

Then you can do something like the following:

    a = open_csv('/home/test_data.csv')

    for i in a:
        print i

    write_csv(a, 'output.csv')

a will be = a list of all the values in the CSV (each row is its own nested list), to write to a CSV, feed the write_csv function a list and then give it an output filename. 
