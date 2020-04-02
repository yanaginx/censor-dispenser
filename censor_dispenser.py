# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import re

print(type(email_one))
def censor_word( text, word_to_censor ):
    text = re.sub(r'\b' + word_to_censor + r'\b', '******', text)
    return text

#print( email_one )
email_one = censor_word( email_one, 'learning algorithms' )
print( email_one )

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
def censor_list_of_words( text, lst_to_censor ):
    title_lst = [word.title() for word in lst_to_censor]
    for word in lst_to_censor: 
        text = re.sub(r'\b' + word + r'\b', '******', text) 
    for word in title_lst:
        text = re.sub(r'\b' + word + r'\b', '******', text)
    return text

#print( email_two )
email_two = censor_list_of_words( email_two, proprietary_terms )
print( email_two )

