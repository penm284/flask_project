# ##function take a string, return the string but reversed
# def flipit(string):
#     newstring = ""
#     for n in string:
#         newstring = n + newstring
#     return newstring
#
# print(flipit("hello"))
#
# ##function takes a string, returns all caps version
# def shout(string):
#     return string.upper()


def gen (DOB):
    message = ""
    if DOB < 1945:
        message = "You are part of the silent generation"
    if DOB > 1977 and DOB < 1995:
        message = "You are a millenial"
    if DOB <=1976 and DOB>1965:
        message = "You are part of gen X"
    if DOB <=1964 and DOB>1946:
        message = "You are a baby boomer"
    if DOB > 1995:
        message = "You are searching outside the parameters"
    return message

# print (gen(DOB))
