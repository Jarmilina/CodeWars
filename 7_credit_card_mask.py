
# Usually when you buy something, you're asked your credit card number,
# phone number or to answer your secret question. 
# However, since someone could look over your shoulder, you don't want it shown on your screen.
# Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.


def maskify(cc): 
    masked_characters = ['#' for x in cc[:-4]]
    mask = "".join(masked_characters) + (cc[-4:])
    print(mask)