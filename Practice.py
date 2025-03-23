ones = {
   'one' : 1,
   'two' : 2,
   'three' : 3,
   'four' : 4,
   'five': 5,
   'six': 6,
   'seven': 7,
   'eight':8,
   'nine': 9,
}

tens = {
   'ten' : 10,
   'twenty' : 20,
   'thirty' : 30,
   'fourty' : 40,
   'fifty': 50,
   'sixty': 60,
   'seventy': 70,
   'eighty':80,
   'ninty': 90,
}

rest = {
   'hundred' : 100,
   'thousand' : 1000,
   'million' : 1000000,
}

in_words = input("Enter any number in words:")

words = in_words.split(" ")
in_numeric = 0
for i in words:
   if i in ones:
      in_numeric += ones[i]
   elif i in tens:
      in_numeric += tens[i]
   elif i in rest:
      in_numeric *= rest[i]
   else:
      pass

print(f"In Words: {in_words} -> Numeric Value: {in_numeric}")
