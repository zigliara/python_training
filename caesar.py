# Caesar Cypher# Function: Encode the textdef encode(file_name, encode_dict, decode_dict):    file_adress = '/Users/maxzigliara/Documents/Kodning/python/' + str(file_name)    encoded_file = '/Users/maxzigliara/Documents/Kodning/python/' + 'Encoded_' + str(file_name)    decoded_file = '/Users/maxzigliara/Documents/Kodning/python/' + 'Decoded_' + str(file_name)    # Encode functionality, from the file name given by the user# The Encoded_file_name is created    with open(encoded_file, 'w') as my_file:        my_source_file = open(file_adress, 'r')        my_text = my_source_file.read()        my_source_file.close()        for letter in my_text:            if ord(letter) != 32: # ASCII for mellanslag                my_file.write(encode_dict[letter])            else:                my_file.write(' ')# Decode functionality, from the Encoded_file_name# The Decoded_file_name is created    with open(decoded_file, 'w') as my_file:        my_source_file = open(encoded_file, 'r')        my_text = my_source_file.read()        my_source_file.close()        for letter in my_text:            if ord(letter) != 32: # ASCII for mellanslag                my_file.write(decode_dict[letter])            else:                my_file.write(' ')    # Create a dictionary for the letters# Keys in the dictionary are letters in the text to encode# Values in the dictionary are the corresponding encoded lettersdef create_dict(offset):    encode_dict = {}    decode_dict= {}    for i in range(97, 123):        if i + offset < 123 and i + offset >= 97:            encode_dict[chr(i)] = chr(i + offset)        elif i + offset >= 123:            encode_dict[chr(i)] = chr(i + offset - 123 + 97)        else: # i + offset < 97: Negative offset            encode_dict[chr(i)] = chr(i + offset + 123 - 97)    # Creating the decode dictionary    for key in encode_dict.keys():        decode_dict[encode_dict[key]] = key    return encode_dict, decode_dict    """Next step is to reverse the dictionary, to decode back the file using the reverse offset.So, using the keys of the old dictionary as the values of the new one, and doing the same thing for the values"""def main():    my_offset = int(input('Give me an offset: '))    my_file = str(raw_input('Give me the name of the file to encode: '))    encode_dict, decode_dict = create_dict(my_offset)    encode(my_file, encode_dict, decode_dict)        if __name__ == "__main__":    main()