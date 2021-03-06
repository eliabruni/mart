import random
import glob, os, shutil, sys


def assign_uuid_to_files(dataset_path, label_file):
    uuid_path = os.path.join(dataset_path, 'uuid')
    os.mkdir(uuid_path)
    os.mkdir(os.path.join(uuid_path, 'labels'))
    os.mkdir(os.path.join(uuid_path, 'images'))
    num_files = len([f for f in os.listdir(os.path.join(dataset_path, 'original-dataset/images'))])
    print num_files
    file_score = {}
    UUIDS = []
    for ii in range(0, num_files):
        UUIDS.append(get_random_string(32))
    UUIDS.sort()

    file = open(label_file, 'r')

    for line in file:
        line = line.split()
        name =  line[0]
        mean =  line[1]
        vari =  line[2]
        file_score[name] = [mean, vari]

    file.close()

    count = 0
    for name in file_score:
        new_label_name     = str(UUIDS[count]) + '.txt'
        new_image_name     = str(UUIDS[count]) + '.jpg'
        new_label_path     = uuid_path + '/labels/' + new_label_name
        old_image_path     = dataset_path + '/original-dataset/images/' + name
        new_image_path     = uuid_path + '/images/' + new_image_name
        label_file         = open(new_label_path, 'w')
        label_file.write(file_score[name][0] + ' ' + file_score[name][1])
        label_file.close()
        shutil.copy(str(old_image_path), new_image_path)
        count += 1

def get_random_string(word_len):
    word = ''
    for i in range(word_len):
        word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    return word

if __name__ =="__main__":
    _dataset_path = sys.argv[1]
    _label_file   = sys.argv[2]
    
    assign_uuid_to_files(_dataset_path, _label_file)
    

    

