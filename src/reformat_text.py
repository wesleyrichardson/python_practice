import re
solution_text = """Jack and Jill were hiking up the hill to buy some mineral water.  Unfortunately, Jack tripped over a pothole in the road, fell down, and broke his smartphone.  “Oh dear!” said Jack.  Well, he actually shouted a stream of expletives their mother wouldn’t approve of, then made some colourful comments about the state of the roads and the local council.  Jill was so shocked she didn’t look where she was going and tumbled down the hill herself.  The pair went home to mend Jack's phone.  Jill suggested putting it in rice.  Jack's response got him grounded for a week, and his phone was never the same again.  """
input_text = """Jack and jill were hiking up the hill to buy some mineral water. Unfortunately, Jack tripped over a pothole in the road,fell down, and broke his smartphone.  “Oh dear!” said jack.Well, he actually shouted a stream of expletives their mother wouldn’t approve of, then made some colourful comments about the state of the roads and the local council.   jill was so shocked she didn’t look where she was going and tumbled down the hill herself; the pair went home to mend Jack's phone .  jill suggested putting it in rice; Jack's response got him grounded for a week, and his phone was never the same again ."""

# Lookup list for proper names
proper_names = {
    "jack": "Jack",
    "jill": "Jill",
}

def replace_semicolons(text):
    return text.replace(';', '.')

def capitalize_names(text):
    for name in proper_names:
        text = text.replace(f"{name}",f"{proper_names[name]}")
    return text

def format_periods(text):
    # Replace all periods with any adjacent space to a period followed by two spaces
    text = re.sub(r'\s*\.\s*', '.  ', text)
    return text

def format_commas(text):
    # Replace all commas with any adjacent space to a comma followed by one space
    text = re.sub(r'\s*\,\s*', ', ', text)
    return text

def capitalize_sentences(text):
    return re.sub(r'(\.)\s*([a-z])', lambda m: m.group(1) + '  ' + m.group(2).upper(), text)

def remove_duplicate_punctuation(text):
    # Define the punctuation characters we want to check for duplicates
    punctuation = r'[.,!?;:]'
    # Use a regular expression to find double instances of punctuation and replace it with one instance
    return re.sub(f'({punctuation})\\1+', r'\1', text)


def format_text(text):
    text = replace_semicolons(text)
    text = capitalize_names(text)
    text = format_periods(text)
    text = format_commas(text)
    text = capitalize_sentences(text)
    text = remove_duplicate_punctuation(text)
    return text


formatted_text = format_text(input_text)

print(formatted_text)
print("\n")
print(solution_text)
print("\n")
if (formatted_text == solution_text):
    print("Data cleansed scucessfully")
else:
    print("Data not cleansed")

# show_differences(formatted_text, solution_text)

