#!/usr/bin/env python

from dictionary import urban_diction
import sys

def main():
  if len(sys.argv) < 2:
    print "Use the correct syntax. ./urban <query string>"
    sys.exit(0)
  query = " ".join(sys.argv[1:])
  urban = urban_diction()
  urban.search(query)

if __name__ == "__main__":
  main()

