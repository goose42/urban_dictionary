from dictionary import urban_diction
import sys

query = sys.argv[1]
 
urban = urban_diction()

urban.search(query)
