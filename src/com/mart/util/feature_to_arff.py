'''
This program is to translate a word co-occurrence matrix of the type
<image feat1, feat2, ..., featN>
to ARFF input format for Weka analysis.
@usage:
Parameter list is described as following:
    @param1: input path (the file containing the features)
    @param2: the name of the feature
    @param3: the length of the feature vector
    @param4: output path

'''
import sys
if __name__ == "__main__":
    IF       = open (sys.argv[1], 'r')
    feature  = sys.argv[2]
    sizefeat = sys.argv[3]

    
    OF = open(sys.argv[4], 'w')
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

