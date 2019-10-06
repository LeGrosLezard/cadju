import glob, os


current_dir = os.path.dirname(os.path.abspath(__file__))

path_data = "data/obj/"
cp=current_dir+"/"+path_data



percentage_test = 30;
file_train = open("train.txt", "w")
file_test = open("test.txt", "w")

counter = 1
index_test = round(100/percentage_test)
for pathAndFilename in glob.iglob(os.path.join(cp, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(cp + title + ".jpg" + "\n")

    else:
        file_train.write(cp + title + ".jpg" +  "\n")
        counter = counter + 1
