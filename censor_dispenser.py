# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

print(type(email_one))
def censor_word( text, word_to_censor ):
    if text.find(word_to_censor) != -1:
        text = text.replace(word_to_censor, '**********')
    return text

email_one = censor_word(email_one, 'learning algorithms')
print(email_one)
