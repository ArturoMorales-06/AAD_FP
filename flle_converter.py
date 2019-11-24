# Module to adapt graph files 

def file_converter(input_file_name, output_file_name):
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    for line in input_file:
        separated_numbers = line.split(',', 2)
        output_file.write(separated_numbers[0] + ' ' + separated_numbers[1])

    input_file.close()
    output_file.close()

def main():
    file_converter('twitter.txt', 'converted_twitter.txt') 

if(__name__ == '__main__'):
    main()