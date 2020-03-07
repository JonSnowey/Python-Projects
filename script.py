# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_this(word):
  global email_one
  if word in email_one:
    email_one = email_one.replace(word,'censored')
    
censor_this('learning algorithms')
email_one_w = open("email_one.txt", "w")
email_one_w.write(email_one)
email_one_w.close()
 
email_one = open("email_one.txt", "r").read()

print(email_one)



def censor_email_2(pro_terms):
  global email_two
  
  for words in pro_terms:
    if words in email_two:
      email_two = email_two.replace(words,'confidential')
    
pro_terms = ["she",'She', "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",'Her', "herself"]
censor_email_2(pro_terms)
email_two_w = open("email_two.txt","w")
email_two_w.write(email_two)
  
email_two_w.close()
  
email_two = open("email_two.txt","r").read()

print(email_two)

#negating negative words and changing them for toned down words.
#censor a word if it occured twice. censor email 3. Also use the previous list on email 3.


def toned_wording(negative_words,pro_terms):

  global email_three
  count = 0 
  
  for words in pro_terms:
    if words in email_three:
      email_three = email_three.replace(words,'confidential')
    for term in negative_words:
      if term in email_three:
        email_three = email_three.replace(term,'doing fine')
      
      
  
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "Horribly", "questionable","HELP"]  
  

toned_wording(negative_words, pro_terms)
email_three_w = open("email_three.txt","w")
email_three_w.write(email_three)
  
email_three_w.close()
  
email_three = open("email_three.txt","r").read()

print(email_three)

 #Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.
  
def censor_all(negative_words,pro_terms):
  global email_four
  
  
  for words in pro_terms:
    if words in email_four:
      email_four = email_four.replace(words,'confidential')
    for term in negative_words:
      if term in email_four:
        email_four = email_four.replace(term,'no issues all good')
  
  
censor_all(negative_words, pro_terms)
email_four_w = open("email_four.txt","w")
email_four_w.write(email_four)
  
email_four_w.close()
  
email_four = open("email_four.txt","r").read()

print(email_four)
  
  
  
  
  
  
  