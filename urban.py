#!/usr/bin/python

from dictionary import urban_diction
import sys

if len(sys.argv) < 2:
  print "Use the correct syntax. ./urban <query string>"
  sys.exit(0)
not_first = 1
search_word = ""
space = ""
for word in sys.argv:
  if not_first > 1:
    search_word += space + word
    space = " "
  not_first +=1

query = search_word

urban = urban_diction()

urban.search(query)
