from Pre_def_funcs import game_cont

def mad_libs():

   story_template = """
      Once upon a time, in a {adjective1} {place}, there was a {adjective2} {noun1} who loved to {verb1}.
      Every day, they would {verb2} with their best friend, a {adjective3} {noun2}.
      One day, they found a {adjective4} {noun3} that could {verb3}!
      Together, they went on an adventure to {place2} and discovered the secret of {plural_noun}.
      They lived {adverb} ever after.
      """

   keywords = [ 
      ("adjective1" , "Enter an adjective: "),
      ("place", "Enter a place: "),
      ("adjective2", "Enter another adjective: "),
      ("noun1", "Enter a noun: "),
      ("verb1", "Enter a verb: "),
      ("verb2", "Enter another verb: "),
      ("adjective3", "Enter another adjective: "),
      ("noun2", "Enter another noun: "),
      ("adjective4", "Enter another adjective: "),
      ("noun3", "Enter another noun: "),
      ("verb3", "Enter another verb: "),
      ("place2", "Enter another place: "),
      ("plural_noun", "Enter a plural noun: "),
      ("adverb", "Enter a adverb")
   ]

   user_format = {}

   for key, values in keywords:
      user_format[key] = input(f'{values}')


   story = story_template.format(**user_format)

   return story

def main():
   game_cont(mad_libs)


if __name__ == "__main__":
   main()
