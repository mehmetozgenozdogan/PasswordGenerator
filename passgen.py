import os
import re
import sys
import time
import random
import hashlib
import logging
from datetime import datetime
filename="./PasswordOutput" + "_" +str(datetime.now().strftime('%Y-%m-%d][%H_%M_%S')) +"].log"
logging.basicConfig(filename=filename, 
                    format='%(message)s', 
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("""
     __________________________________________________________________________
    |                                                                          |
    |    Title       : Password Generator                                      |
    |    Description : Enter your keywords with comma(,) or space( ) seperator |
    |                  and get your strong password                            |
    |__________________________________________________________________________|
    |                                                                          |
    |    Author      : Memonet                                                 |
    |    Date        : 2021-04-24                                              |
    |    Location    : Ankara/TURKEY                                           |
    |    Version     : v1.0.0.0                                                |
    |    Filename    : passgen.py                                              |
    |__________________________________________________________________________|

""")

print ("""
     __________________________________________________________________________
    |                                                                          |
    |    Title       : Password Generator                                      |
    |    Description : Enter your keywords with comma(,) or space( ) seperator |
    |                  and get your strong password                            |
    |__________________________________________________________________________|
    |                                                                          |
    |    Author      : Memonet                                                 |
    |    Date        : 2021-04-24                                              |
    |    Location    : Ankara/TURKEY                                           |
    |    Version     : v1.0.0.0                                                |
    |    Filename    : passgen.py                                              |
    |__________________________________________________________________________|

""")

keyword_input = input('Please Input Your Keywords       : ')
password_length = int(input('Please Input Your Password Length: '))
password_count = int(input('Please Input Your Password Count : '))
password_special_charset = ["!","*",".",",","#","$","?","-","+"]
#password_length = 12
#password_count = 5

def keyword_splitter(keyword_input):
    #This function make split string text using comma seperator
    #Return keywords array
    if keyword_input == None:
        return None
    else:
        keywords = []
        try:
            keywords = list(filter(None, re.split(',|\s',keyword_input)))
            return keywords
        except:
            return keyword_input
    
def keyword_changer(keywords):
    #This function makes keywords more strong
    # Ex: test:t35t
    # abcdefghijklmnoprstuvxyz
    # ''  '
    #Check Upper and Lower case
    if keywords == None:
        return None
    else:
        keyword_tmp = []
        for keyword in keywords:
            if "e" in keyword or "E" in keyword:
                # e = 3 or E = 3
                keyword = keyword.replace("E","3")
                keyword = keyword.replace("e","3")

            if "s" in keyword or "S" in keyword:
                # s = 5 or S = 5
                keyword = keyword.replace("s","5")
                keyword = keyword.replace("S","5")

            if "a" in keyword or "A" in keyword:
                # a = @ or A = 4 
                keyword = keyword.replace("a","@")
                keyword = keyword.replace("A","4")

            if "o" in keyword or "O" in keyword:
                # o = 0 or O = 0
                keyword = keyword.replace("o","0")
                keyword = keyword.replace("O","0")
                
            if "b" in keyword or "B" in keyword:
                # b = 6 or B = 8
                keyword = keyword.replace("b","6")
                keyword = keyword.replace("B","8")

            if "l" in keyword or "L" in keyword:
                # l = 1 or L = 2
                keyword = keyword.replace("l","1")
                keyword = keyword.replace("L","2")
            
            if "i" in keyword or "I" in keyword:
                # i = ! or I = !
                keyword = keyword.replace("i","!")
                keyword = keyword.replace("I","!")

            if keyword.isupper() == True:
                keyword = keyword[0].lower() + keyword[1:]
            elif keyword.islower() == True:
                keyword = keyword[0].upper() + keyword[1:]

            keyword_tmp.append(keyword)
        return keyword_tmp
    
def password_generator(keywords):
    #This function generate random password using modified keywords
    #Password Gnenerator function return 12 character password
    if keywords == None:
        return None
    else:
        password_string = ""    
        for i in range (0, 3):
            password_A = str(password_special_charset[random.randint(0, len(password_special_charset) - 1)]) 
            password_B = str(keywords[random.randint(0, len(keywords) - 1)]) 
            password_C = str(password_special_charset[random.randint(0, len(password_special_charset) - 1)]) 
            password_D = str(keywords[random.randint(0, len(keywords) - 1)]) 
            password_string = password_string + password_A + password_B + password_C + password_D

        if len(password_string) > password_length:
            password_string = password_string[0:password_length]
        elif len(password_string) < password_length:
            password_generator(keywords)
        return password_string

def password_hasher(password):
    #SHA-512 and encode utf-8 password hasher
    if password == None:
        return None
    else:
        password_hash = hashlib.sha512(password.encode('utf-8'))
        return password_hash.hexdigest()

def password_quality(password):
    #This function checks password using some criterias
    # Upper/Lower keys, Number, etc.
    return password

logger.debug("     ___________________")
print ("     ___________________")
start_time = time.time()
start_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
logger.debug("    |Starting Date      : " + start_date)
print ("    |Starting Date      : " + start_date)

logger.debug("     ___________________")
print ("     ___________________")
logger.debug("    |Password Length    : " + str(password_length))
print ("    |Password Length    : " + str(password_length))

logger.debug("    |Password Count     : " + str(password_count))
print ("    |Password Count     : " + str(password_count))


logger.debug("     ___________________")
print ("     ___________________")
first_keywords = keyword_splitter(keyword_input)
logger.debug("    |Entered Keywords   : " + str(first_keywords))
print ("    |Entered Keywords   : " + str(first_keywords))

logger.debug("     ___________________")
print ("     ___________________")
last_keywords = keyword_changer(first_keywords)
logger.debug("    |Changed Keywords   : " + str(last_keywords))
print ("    |Changed Keywords   : " + str(last_keywords))

logger.debug("     _________________________")
print ("     _________________________")
logger.debug("    |PASSWORD(s) GENERATING...")
print ("    |PASSWORD(s) GENERATING...")

for i in range (0, password_count):
    password_tmp = password_generator(last_keywords)
    logger.debug("    |Generated Password : " + str(password_tmp))
    print ("    |Generated Password : " + str(password_tmp))
    #password_tmp_hash = password_hasher(password_tmp)
    #logger.debug("    |Password SHA-512   : " + str(password_tmp_hash))
    #print ("    |Password SHA-512   : " + str(password_tmp_hash))

logger.debug("     _____________________________________")
logger.debug("    | PASSWORD(s) GENERATED SUCCESSFULLY! |")
logger.debug("    | Operation Time     : %.4f seconds |" % (time.time() - start_time))
logger.debug("    |_____________________________________|")

print ("     _____________________________________")
print ("    | PASSWORD(s) GENERATED SUCCESSFULLY! |")
print ("    | Operation Time     : %.4f seconds |" % (time.time() - start_time))
print ("    |_____________________________________|")

print ("Create Log file for strong passwords >> " + str(filename))
input ("Press any key for Exit")
