import hashlib
from urllib.request import urlopen
from replit import clear


# reads word list but raise exception if error
def readwordlist(url):
  try:
    wordlistfile = urlopen(url).read()
  except Exception as e:
    print("Hey there was some error while reading the worlist, error: ", e)
    exit()
  return wordlistfile


# returns a string for the hash of a password
def hash(password):
  result = hashlib.sha1(password.encode())
  return result.hexdigest()


# checks whether actual password hash matches passwordlist hash
def bruteforce(guesspasswordlist, actual_password_hash):
  for guesspassword in guesspasswordlist:
    if hash(guesspassword) == actual_password_hash:
      print(f"Password: {guesspassword}\n Please change this, as it was really easy to guess it!")
      exit()


def main():
  wordlisturl = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
  wordlist = readwordlist(wordlisturl).decode("UTF-8")
  guesspassword_list = wordlist.split("\n")

  actual_password = input("Password (find if your password is safe!): ")
  clear()
  
  actual_password_hash = hash(actual_password)
  
  bruteforce(wordlist.splitlines(), actual_password_hash)
  # if password not in list
  print("I couldn't guess! You have a strong password!")


main()