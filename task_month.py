month={ 'jan':'hi january',
        'feb':'hi february',
        'mar':'hi march',
        'apr':'hi april',
        'may':'hi may',
        'jun':'hi june',
        'jul':'hi july',
        'aug':'hi august',
        'sep':'hi september',
        'oct':'hi october',
        'nov':'hi november',
        'dec':'hi december'
}

def jan(dict):
  print(dict['jan'])

def feb(dict):
  print(dict['feb'])

def mar(dict):
    print(dict['mar'])

def apr(dict):
  print(dict['apr'])

def may(dict):
  print(dict['may'])

def jun(dict):
  print(dict['jun'])


def jul(dict):
    print(dict['jul'])

def aug(dict):
  print(dict['aug'])

def sep(dict):
  print(dict['sep'])


def oct(dict):
    print(dict['oct'])


def nov(dict):
    print(dict['nov'])

def dec(dict):
  print(dict['dec'])

print("Displaying msg using separate functions for each month:")
jan(month)
feb(month)
mar(month)
apr(month)
may(month)
jun(month)
jul(month)
aug(month)
sep(month)
oct(month)
nov(month)
dec(month)


print("Displaying msg using only one function:")
def print_msg(dict):
    for k,v in dict.items():
        print(v)

print_msg(month)

print("Displaying only the month's names:")

def months(dict):
    for m in dict:
        print(m)

months(month)

print("Displaying only the messeges:")

def msg(dict):
    for k,v in dict.items():
        print(v)

msg(month)

