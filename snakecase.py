def snake_to_camel(string):
  camel = []
  words = string.split("_")
  # first word is beginning of camelcase
  camel.append(words[0])
  for word in words[1:]:
      capital = word[0].upper()
      word = capital + word[1:]
      camel.append(word)

  return "".join(camel)


















