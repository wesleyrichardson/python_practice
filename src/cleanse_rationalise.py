datalist = [["16", "10", "8", "3", "7"],["8", "09", "19", "20", "4"],["Sechs", "Acht", "Sechzehn", "Funf", "null"],["1", "30", "2", "5", "7"],["Vierzehn", "Eins", "zwei", "Neun", "Drei"],["six", "neuf", "seize", "zero",""],["fourteen", "Eleven", "Forteen", "eight", "Twenty"],["Douze", "Onze", "Huit", "Quinze", "Sept"],["018", "09", "09", "022", "04"],["un", "trois", "quatorze", "dix-huit", "vingt"],["Five", "Three", "Nineteen", "Twenty", "zero"],["einundzwanzig", "Vierzehn", "Eins", "zwei","Vier"]]

# Dictionaries for word-to-number conversion
english_numbers = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20
}

french_numbers = {
    'zéro': 0, 'un': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6, 'sept': 7, 'huit': 8, 'neuf': 9, 'dix': 10,
    'onze': 11, 'douze': 12, 'treize': 13, 'quatorze': 14, 'quinze': 15, 'seize': 16, 'dix-sept': 17, 'dix-huit': 18, 'dix-neuf': 19, 'vingt': 20
}

german_numbers = {
    'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4, 'funf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9, 'zehn': 10,
    'elf': 11, 'zwolf': 12, 'dreizehn': 13, 'vierzehn': 14, 'fünfzehn': 15, 'sechzehn': 16, 'siebzehn': 17, 'achtzehn': 18, 'neunzehn': 19, 'zwanzig': 20
}


# Function to convert words in datalist to lowercase
def convert_to_lowercase(datalist):
    lowercase_datalist = []
    for sublist in datalist:
        lowercase_sublist = []
        for word in sublist:
            lowercase_word = word.lower()
            lowercase_sublist.append(lowercase_word)
        lowercase_datalist.append(lowercase_sublist)
    return lowercase_datalist


# Function to extract the integer value from a data entry
def word_to_number(word):
    word = word.lower()
    if word in english_numbers:
        return english_numbers[word]
    elif word in french_numbers:
        return french_numbers[word]
    elif word in german_numbers:
        return german_numbers[word]
    else:
        return None
    
#Process individual data point
def process_data_value(value):
    if value.isdigit():
        num = int(value)
    else:
        num = word_to_number(value)
    
    if num is not None and (0 <= num <= 20):
        return num
    else:
        return None

#Process a data subset
def process_data_set(data_set):
    converted_set = [process_data_value(value) for value in data_set]
    if None in converted_set or len(converted_set) != 5:
        return None
    return converted_set
    
#Process a data list of data subsets
def process_data_list(datalist):
    datalist = convert_to_lowercase(datalist)
    valid_data = []
    invalid_data = []
    
    for data_set in datalist:
        processed_set = process_data_set(data_set)
        if processed_set:
            valid_data.append(processed_set)
        else:
            invalid_data.append(data_set)
    
    return valid_data, invalid_data

#Test the function 

valid_data, invalid_data = process_data_list(datalist)
print(f"\nValid Data: {valid_data}\n")
print(f"Invalid Data{invalid_data}")