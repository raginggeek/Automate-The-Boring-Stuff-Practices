#! python3

import pyperclip
import re

# Create a regex for phone
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d{3})|(\(\d{3}\)))?        # area code (optional)
(\s|-)                        # first seperator
\d{3}                         # first 3 digits
-                             # seperator
\d{4}                         # last 4 digits
(((ext(\.)?\s)|x) (\d{2,5}))? # extension (optional)
) 
''', re.VERBOSE)

# create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+ # name part
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# Extract emails and phones off the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy the extracts to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
