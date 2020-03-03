import re

# Searching index
text = "This is a string with term1, but not the other!"

match =  re.search("term1",text)
print(match.start())

# Split

split_term = "@"
email = "user@gmail.com"

print(re.split(split_term,email))

# Find All

print(re.findall("match","test phrase match in match middle"))

# Examples

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ["sd*"] #s followed by 0 or more d's
multi_re_find(test_patterns,test_phrase)

test_patterns = ["sd+"] #s followed by 1 or more d's
multi_re_find(test_patterns,test_phrase)

test_patterns = ["sd?"] #s followed by 0 or 1 d's
multi_re_find(test_patterns,test_phrase)

test_patterns = ["sd{3}"] #s followed by 3 d's
multi_re_find(test_patterns,test_phrase)

test_patterns = ["sd{1,3}"] #s followed by 1 or 3 d's
multi_re_find(test_patterns,test_phrase)

test_patterns = ["s[sd]+"] #s followed by 1 or more s's or d's
multi_re_find(test_patterns,test_phrase)

# Removing terms
test_phrase = "This is a string! But it has pontuation. How can we remove it?"
test_patterns = ["[^!.?]+"]
multi_re_find(test_patterns, test_phrase)

test_patterns = ["[a-z]+"] # Sequences of lower case characters
multi_re_find(test_patterns, test_phrase)

test_patterns = ["[A-Z]+"] # Sequences of upper case characters
multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string with number 12312 and a symbol #hashtag"
test_patterns = [r'\d+'] # Sequences of numbers (digits)
multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string with number 12312 and a symbol #hashtag"
test_patterns = [r'\D+'] # Sequences of not-numbers
multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string with number 12312 and a symbol #hashtag"
test_patterns = [r'\s+'] # Sequences of white spaces
multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string with number 12312 and a symbol #hashtag"
test_patterns = [r'\S+'] # Sequences of not-white spaces
multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string with number 12312 and a symbol #hashtag"
test_patterns = [r'\w+'] # Sequences of alpha-numeric
multi_re_find(test_patterns, test_phrase)

test_phrase = "This is a string with number 12312 and a symbol #hashtag"
test_patterns = [r'\W+'] # Sequences of non-alpha-numeric
multi_re_find(test_patterns, test_phrase)
