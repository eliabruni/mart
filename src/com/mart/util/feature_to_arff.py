'''
This program is to translate a word co-occurrence matrix of the type
<word feat1, feat2, ..., featN>
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

   	














    F1.close()
    #combine with next files
    mark = {}
    for i in range(3,2 + N):
        F = open (sys.argv[i], 'r')
        old_sizefeat = sizefeat
        mark.clear()
        for line in F:
            line = line.strip()
            if sizefeat == old_sizefeat:
                sizefeat = sizefeat + line.count(' ')

            sep = line.find(' ', 0)
            word = line[0:sep]
            feat = line[sep:]
            if word in hash:
                hash[word] += feat
                mark[word] = True
            else:
                oldfeature = ''
                for j in range(0, old_sizefeat):
                    oldfeature += ' 0'
                hash[word] = oldfeature + feat
		mark[word] = True
        
        for wordleft in hash.keys():
            if not wordleft in mark:
                newfeature = ''
                for j in range(old_sizefeat, sizefeat):
                    newfeature += ' 0'
                hash[wordleft] += newfeature
        F.close()

    #write the output
    FO = open(sys.argv[N+2], 'w')

    for word in hash.keys():
        FO.write(word)
        FO.write(hash[word] + '\n')
    FO.close()

