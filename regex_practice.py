import re

#? 1 or 0 times
#* 0 or more times
#+ 1 or more times

#[] indicates a set of chars
#[^ab] inverts the set === every char except 'a' or 'b'


def find_word(phrase, substr):
    match = re.search(re.escape(substr) + r'\w*', phrase)
    if match:
        print('found: {0}'.format(match.group()))
    else:
        print('did not find \'{}\''.format(substr))

def find_emails(txt):
    emails = re.findall(r'[\w.-]+@[\w.-]+', txt)
    if emails:
        for email in emails:
            print(email)
    else:
        print('no emails')

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
find_emails(str)

# phrase = input('Enter phrase: ')
# substr = input('Enter search term: ')
# find_word(phrase, substr)

# text = input('Enter text: ')
# find_emails(text)
