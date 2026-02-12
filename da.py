try:
    import Tkinter as tk
except:
    import tkinter as tk


# GUI development code

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DOCUMENT ANALYSER")
        self.root.geometry('500x300')
        
# 1. Welcome Button widget       
        tk.Button(self.root, text="Welcome to NEW HORIZON", fg="blue", bg="white", font=("Arial", 16)).pack()
# 2. Image widget       
        photo= tk.PhotoImage(file=r"C:\Users\Shreya\Desktop\image\nhce_2p.png")
        photoimage=photo.subsample(5,5)
   
        redbutton = tk.Button(self.root, text="Welcome to NEW HORIZON", image=photoimage, fg="blue", 
                              bg="white", font=("Arial", 16))
        redbutton.pack()
# 3. Continue... button widget
        button = tk.Button(self.root,
                           text='Click to Continue...',fg="red",
                           command=self.quit)
        button.pack()
     
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

app = Test()


#Import NLTK libraries

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names


def word_feats(words):
    return dict([(word, True) for word in words])

positive_vocab = ['awesome', 'liked', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
neutral_vocab = ['book', 'the', 'sound', 'i', 'it', 'was', 'is', 'actors', 'did', 'movie', 'know', 'words', 'parts', 'and', 'are', 'little', 'but', 'some', '..', '...']
negative_vocab = ['bad', 'terrible', 'useless', 'hate', 'worst']

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

# preparation of training set

train_set = negative_features + positive_features + neutral_features

# train the classifier using training set:

classifier = NaiveBayesClassifier.train(train_set)

# Predict
neg = 0
pos = 0
neu = 0

#Reading source input file
source_file = "C:/Users/Shreya/Desktop/image/review1.txt"
file1 = open(source_file,"r")
sentence = file1.readline()
print(sentence)

# Convert UPPER case to LOWER case
sentence = sentence.lower()

words = sentence.split(' ')
print(words)

# validation and clustering of words
for word in words:
    classResult = classifier.classify(word_feats(word))
    print(classResult)
    if classResult == 'pos':
        pos = pos + 1
    if classResult == 'neg':
        neg = neg + 1
    if classResult == 'neu':
        neu = neu + 1

print('\nNo. of negative words:', neg)
print('No. of positive words:', pos)
print('No. of neutral words:', neu)


# graphical representation
import matplotlib.pyplot as plt

x=["positive","negative"]
y=[pos,neg]

plt.title("POSITIVE - NEGATIVE BAR GRAPH")
plt.ylabel("Count   ->")
plt.xlabel("Positive/Negative words   ->")

ax=plt.gca()
ax.tick_params(axis='x',colors='blue')
ax.tick_params(axis='y',colors='red')

plt.bar(x,y,color= ['blue','red'],width = 0.3)

plt.show()
#plt.savefig('temp.png')


# Actions based on Business requirements
# Copy review to the respective folder
import shutil

pos_file_path= "C:/Users/Shreya/Desktop/image/positive/"
neg_file_path= "C:/Users/Shreya/Desktop/image/negative/"

print("\n")
if(pos>neg):
    print("It is a postive review.")
    shutil.copy2(source_file,pos_file_path)
else:
    print("It is a negative review.")
    shutil.copy2(source_file,neg_file_path)
