#!/usr/bin/python

import csv
import os


# def open_csv(input_file, output):
def open_csv(input_file):

    fn = os.path.join(os.path.dirname(__file__), input_file)

    with open(fn, 'rb') as f_input:

        reader = csv.reader(f_input)

        rows_list = []

        for i in reader:

            rows_list.append(i)

        return rows_list


def write_csv(output_content, output_file):

    with open(output_file, 'wb') as f_output:
        writer = csv.writer(f_output)
        writer.writerows(output_content)

if __name__ == '__main__':

    a = open_csv('/home/schuyler/Work/awis_project/upload_to_ch/test_data.csv')

    for i in a:
        print i

    write_csv(a, 'output.csv')
