'''
This program is to translate a word co-occurrence matrix of the type
<image feat1, feat2, ..., featN>
to ARFF input format for Weka analysis.
@usage:
Parameter list is described as following:
    @param1: feature file
    @param2: output

'''
import sys
if __name__ == "__main__":
    sizefeat = 0
    IF       = open (sys.argv[1], 'r')
    feature  = sys.argv[2]

    # TODO:
    # find a way to have only the first line of the file to have the number of features
    sizefeat = line.count(' ')
    
    OF = open(sys.argv[3], 'w')
    OF.write('@RELATION ' + feature + '\n')
    OF.write('\n')

    idx = 0
    for feat in range(sizefeat):
   	OF.write('@ATTRIBUTE ' + str(idx) + ' NUMERIC' + '\n'
	idx += 1
    
    OF.write('\n') 
    OF.write('@DATA' + '\n') 
    
    for line in IF:
        line     = line.strip()
	word     = line[0]
	features = array(line[1:], dtype=float32)
	for feat in features:
	    OF.write(str(feat) + ',')
	OF.write('\n') 
    OF.close()	

