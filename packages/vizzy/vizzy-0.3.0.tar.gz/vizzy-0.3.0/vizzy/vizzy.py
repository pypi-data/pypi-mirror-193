import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer
import gensim
from collections import  Counter
import string
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import word_tokenize
import pyLDAvis
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
from spacy import displacy
import nltk
from textblob import TextBlob
from textstat import flesch_reading_ease
import gensim.corpora as corpora
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from pprint import pprint
import spacy
import pickle
import re
import pyLDAvis
import pyLDAvis.gensim_models
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity



plt.rcParams.update({'font.size': 18})
plt.rcParams.update({'figure.figsize': [16, 12]})
plt.style.use('seaborn-whitegrid')


# In[ ]:


class vizzy_sentence:
    '''The following function creates an object for visualization with the below functions.
    Parameters
    -------
    data = Pandas DataFrame
    column = str
    split = str
    
    returns
    --------
    object (with added column which is the text with the stopwords removed)'''
    def __init__(self, data, column, split=None):
        from nltk.corpus import stopwords
        stop = set(stopwords.words('english'))
        '''create text_without_stopwords column for later use'''
        data['text_without_stopwords'] = data[column].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop]))
        self.data = data
        self.column = column
        self.split = split
        
        
    
    '''The following function creates histograms for your text data. Each histogram shows the length of data column in characters. If you intialized your object with a split, this function will show histograms for each split in your data.
    parameters
    ---------
    split1 = string of one of the values in your split column
    split2 = string value of the second value in your split column
    
    returns
    --------
    histograms'''
    def show_char_count(self, split1=None, split2=None):
        '''Histogram of the length of your data column in characters'''    
        '''Plot the histogram for all values'''
        plt.hist(self.data[self.column].str.len(), bins=20, color='blue', alpha=0.5, label='All')

        '''Plot the histogram for split1 values'''
        plt.hist((self.data[self.column][self.data[self.split]==split1].str.len()), bins=20, color='green', alpha=0.5, label=str(split1))
        
        '''Plot the histogram for split2 values'''
        plt.hist((self.data[self.column][self.data[self.split]==split2].str.len()), bins=20, color='red', alpha=0.5, label=str(split2))

        # Add the labels and title
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histograms of Value')

        # Show the legend
        plt.legend()

        # Show the plot
        plt.show()
        
        
    '''The following function does the same thing as the show_char_count function, only it prints the data rather than creating a histogram. This function will not split the data.
    parameters
    ---------
    none
    
    returns
    ---------
    output of character count'''    
    def print_char_count(self):
        '''Print average character count per text cell'''
        def average(numbers):
            avg = sum(numbers)/len(numbers)
            return avg
        counts = [len(word) for word in self.data[self.column]]
        print("The average number of characters in your text is {}".format(average(counts)))
        print("The max number of characters in your text is {}".format(max(counts)))
        print("The smallest number of characters in your text is {}".format(min(counts)))
    
    
    
    
    
    
    '''The following function creates histograms for your text data. Each histogram shows the length of the words in your data column in words. If you intialized your object with a split, this function will show histograms for each split in your data.
    parameters
    ---------
    split1 = string of one of the values in your split column
    split2 = string value of the second value in your split column
    
    returns
    --------
    histograms'''
    def show_word_count(self, split1=None, split2=None):
        '''Histogram of the length of data column in words'''
        plt.hist(self.data[self.column].str.split().map(lambda x: len(x)), bins = 20, color='blue', alpha=0.5, label='All')
        '''Plot histogram for train values'''
        plt.hist(self.data[self.data[self.split] == split1][self.column].apply(lambda x: len(x.split())), bins = 20, color='green', alpha=0.5, label=str(split1))        
        '''Plot histogram for test values'''
        plt.hist(self.data[self.data[self.split] == split2][self.column].apply(lambda x: len(x.split())), bins = 20, color='red', alpha=0.5, label=str(split2))        
        '''Add labels and title'''
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Word Count')
        
        '''Show the legend'''
        plt.legend()                                 
        
        '''Show the plot'''
        plt.show()
        
        
        
        
    '''The following function does the same thing as the show_word_count function, only it prints the data rather than creating a histogram. This function will not split the data.
    parameters
    ---------
    none
    
    returns
    ---------
    output of character count'''                                          
    def print_word_count(self):
        '''Print length of data column in words'''
        def average(numbers):
            avg = sum(numbers)/len(numbers)
            return avg
        print("The average number of words in your text cells is {}".format(average(self.data[self.column].str.split().map(lambda x: len(x)))))
        print("The max number of words in your text cells is {}".format(max((self.data[self.column].str.split().map(lambda x: len(x))))))
        print("The smallest number of words in your text cells is {}".format(min((self.data[self.column].str.split().map(lambda x: len(x))))))
        
        
        
        
        
    '''The following function creates histograms for your text data. Each histogram shows the length of the words in your data column in characters. If you intialized your object with a split, this function will show histograms for each split in your data.
    parameters
    ---------
    split1 = string of one of the values in your split column
    split2 = string value of the second value in your split column
    
    returns
    --------
    histograms'''        
    def show_word_length(self, split1=None, split2=None):
        '''Hist of length of words in data column in characters'''
        plt.hist(self.data[self.column].str.split().apply(lambda x: [len(i) for i in x]).map(lambda x: np.mean(x)), bins = 20, color='blue', alpha=0.5, label='All')
        '''Plot histogram for values where the value in the split column is equal to split1'''
        plt.hist(self.data[self.data[self.split] == split1][self.column].str.split().apply(lambda x: [len(i) for i in x]).map(lambda x: np.mean(x)), bins = 20, color='green', alpha=0.5, label=str(split1))        
        '''Plot histogram for values where the value in the split column is equal to split2'''
        plt.hist(self.data[self.data[self.split] == split2][self.column].str.split().apply(lambda x: [len(i) for i in x]).map(lambda x: np.mean(x)), bins = 20, color='red', alpha=0.5, label=str(split2))        
        '''Add labels and title'''
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Word Length')
        '''Show legend'''
        plt.legend()                                 
        '''show plot'''                                
        plt.show()

        
        
    '''The following function does the same thing as the show_word_length function, only it prints the data rather than creating a histogram. This function will not split the data.
    parameters
    ---------
    none
    
    returns
    ---------
    output of character count'''   
    def print_word_length(self):
        '''Print length of words in data in characters'''
        def average(numbers):
            avg = sum(numbers)/len(numbers)
            return avg
        avg_len = self.data[self.column].str.split().apply(lambda x : [len(i) for i in x]).map(lambda x: np.mean(x))
        max_len = self.data[self.column].str.split().apply(lambda x: [len(i) for i in x]).map(lambda x: np.max(x))
        min_len = self.data[self.column].str.split().apply(lambda x: [len(i) for i in x]).map(lambda x: np.min(x))
        print("The average number of characters of the words in your text cells is {}".format(average(avg_len)))
        print("The max number of characters of the words in your text cells is {}".format(max(max_len)))
        print("The smallest number of characters of the words in your text cells is {}".format(min(min_len)))

        
        
        
    '''This function shows you the most common stopwords in your text data using NLTK's stopwords list.
    parameters
    --------
    None
    
    returns
    --------
    bar graph showing most common stopwords in data'''
    def show_common_stopwords(self):
        '''List of common stopwords in data'''
        stop = set(stopwords.words('english'))
        corpus=[]
        new= self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word.lower() for i in new for word in i]
        from collections import defaultdict
        dic=defaultdict(int)
        for word in corpus:
            if word in stop:
                dic[word]+=1
        top=sorted(dic.items(), key=lambda x:x[1],reverse=True)[:10] 
        x,y=zip(*top)
        plot = plt.bar(x,y)
        return plot
    

    
    
    
    
    
    '''This function prints the output of the most common stopwords in your text data using NLTK's stopwords list.
    parameters
    ---------
    None
    
    returns
    -------
    output of most common stopwords'''
    def print_common_stopwords(self):
        '''Print top 10 common stopwords'''
        stop=set(stopwords.words('english'))
        corpus=[]
        new= self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word.lower() for i in new for word in i]

        from collections import defaultdict
        dic=defaultdict(int)
        for word in corpus:
            if word in stop:
                dic[word]+=1
        top=sorted(dic.items(), key=lambda x:x[1],reverse=True)[:10] 
        x,y=zip(*top)
        print("The most common stopwords in your text cells are:")
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
    
    
    
    
    
    
    
    '''This function shows the most common words in your data that arent stopwords in a bar chart.
    parameters
    --------
    None
    
    returns
    --------
    output of most common non-stopwords as a bar chart'''
    def show_common_words(self):
        '''Common words in data'''
        stop = set(stopwords.words('english'))
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word.lower() for i in new for word in i]
        counter=Counter(corpus)
        most=counter.most_common()
        x, y=[], []
        for word,count in most[:40]:
            try:
                if (word not in stop):
                    x.append(word)
                    y.append(count)
            except:
                x.append(word)
                y.append(count)
        sns.barplot(x=y,y=x)
    
    
    
    
    
    
    
    '''This function prints the most common stopwords in your text data for each defined split.
    parameters
    ---------
    self.split != None
    split1 = string value of first value in split column
    split2 = string value of other value in split column
    
    returns
    --------
    output of most common stopwords for each split in your text data'''
    def print_common_words_split(self, split1=None, split2=None):
        '''Prints top 20 most common words in corpus from split1'''
        stop = set(stopwords.words('english'))

        corpus=[]
        new=self.data[self.data[self.split]==split1][self.column].str.split()
        new=new.values.tolist()
        corpus=[word.lower() for i in new for word in i]
        counter=Counter(corpus)
        most=counter.most_common()
        x, y=[], []
        for word,count in most[:40]:
            try:
                if (word not in stop):
                    x.append(word)
                    y.append(count)
            except:
                x.append(word)
                y.append(count)
        print("Most common words in {}".format(split1))
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
        print("\n")

        '''Prints top 20 most common words in corpus from split2'''
        stop = set(stopwords.words('english'))

        corpus=[]
        new=self.data[self.data[self.split]==split2][self.column].str.split()
        new=new.values.tolist()
        corpus=[word.lower() for i in new for word in i]
        counter=Counter(corpus)
        most=counter.most_common()
        x, y=[], []
        for word,count in most[:40]:
            try:
                if (word not in stop):
                    x.append(word)
                    y.append(count)
            except:
                x.append(word)
                y.append(count)
        print("Most common words in {}".format(split2))
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))

        
    '''This function prints the top 20 most common words that aren't stopwords in your text data. This function does not split your data.
    parameters
    --------
    None
    
    returns
    --------
    output of your most common non-stopwords in your text data'''
    def print_common_words(self):
        '''Prints top 20 most common words in corpus'''
        stop = set(stopwords.words('english'))

        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word.lower() for i in new for word in i]
        counter=Counter(corpus)
        most=counter.most_common()
        x, y=[], []
        for word,count in most[:40]:
            try:
                if (word not in stop):
                    x.append(word)
                    y.append(count)
            except:
                x.append(word)
                y.append(count)
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))    
     
    
    
    
    
    
    '''This function uses TextBlob to find the average sentiment of your text data.
    parameters
    --------
    None
    
    returns
    --------
    histogram showing the sentiment in your data'''
    def show_sentiment(self):
        '''Sentiment in data'''
        text = self.data[self.column]
        def polarity(text):
            return TextBlob(text).sentiment.polarity
        self.data['polarity_score']=self.data[self.column].apply(lambda x : polarity(x))
        hist = self.data['polarity_score'].hist()
        return hist

    
    
    
    
    
    
    '''This function uses TextBlob to group the text in your data into "positive", "neutral", and "negative" sentiments and creates a bar graph for you to visualize.
    parameters
    --------
    None
    
    returns
    --------
    bar graph showing sentiment of your text data'''
    def show_sentiment_cats(self):
        '''Plot data by sentiment (pos, neu, neg)'''
        def polarity(text):
            return TextBlob(text).sentiment.polarity
        self.data['polarity_score']=self.data[self.column].apply(lambda x : polarity(x))
        def sentiment(x):
            if x<0:
                return 'neg'
            elif x==0:
                return 'neu'
            else:
                return 'pos'
        self.data['polarity']=self.data['polarity_score'].map(lambda x: sentiment(x))
        plot = plt.bar(self.data.polarity.value_counts().index, self.data.polarity.value_counts())
        return plot
    
    

    
    
    
    
    '''This function uses TextBlob to identify the top 5 text entries in your data that have a negative sentiment.
    Parameters
    ----------
    None

    Returns
    -------
    Output containing the top 5 text entries that have a negative sentiment.'''
    def print_neg_sentiment(self):
        '''Show negative sentiment'''
        def polarity(text):
            return TextBlob(text).sentiment.polarity
        self.data['polarity_score']=self.data[self.column].apply(lambda x : polarity(x))
        def sentiment(x):
            if x<0:
                return 'neg'
            elif x==0:
                return 'neu'
            else:
                return 'pos'
        self.data['polarity']=self.data['polarity_score'].map(lambda x: sentiment(x))
        results = self.data[self.data['polarity']=='neg'][self.column].head(5)
        return results
    
    
    
    
    
    
    '''This function uses TextBlob to identify the top 5 text entries in your data that have a positive sentiment.
    Parameters
    ----------
    None

    Returns
    -------
    Output containing the top 5 text entries that have a positive sentiment.'''
    def print_pos_sentiment(self):
        '''Show positive sentiment'''
        def polarity(text):
            return TextBlob(text).sentiment.polarity
        self.data['polarity_score']=self.data[self.column].apply(lambda x : polarity(x))
        def sentiment(x):
            if x<0:
                return 'neg'
            elif x==0:
                return 'neu'
            else:
                return 'pos'
        self.data['polarity']=self.data['polarity_score'].map(lambda x: sentiment(x))
        results = self.data[self.data['polarity']=='pos'][self.column].head(5)
        return results
    
    
    
        
    
    '''This function shows a histogram of the Flesch-Kincaid score for your text data.

    Parameters:
    ----------
    split1: str, optional
        The name of the first dataset split.
    split2: str, optional
        The name of the other dataset split.

    Returns:
    -------
    A matplotlib histogram that visualizes the Flesch-Kincaid score distribution of the text data in your dataset.'''
    def show_flesch_kincaid(self, split1=None, split2=None):
        '''show flesch kincaid score'''
        plt.hist(self.data[self.column].apply(lambda x : flesch_reading_ease(x)))
        '''Show histogram for train values'''
        plt.hist(self.data[self.data[self.split] == split1][self.column].apply(lambda x: flesch_reading_ease(x)), bins = 20, color='red', alpha=0.5, label=str(split1))        
        '''Show histogram for test values'''
        plt.hist(self.data[self.data[self.split] == split2][self.column].apply(lambda x: flesch_reading_ease(x)), bins = 20, color='red', alpha=0.5, label=str(split2))        
        
    
    
    
    
    
    
    '''This function shows the output of the Flesch-Kincaid min, max, and average scores for your text data.

    Parameters:
    ----------
    split1: str, optional
        The name of the first dataset split.
    split2: str, optional
        The name of the other dataset split.

    Returns:
    -------
    Text output of the Flesch-Kincaid score min, max, and average of the text data in your dataset.'''
    def print_flesch_kincaid(self):
        '''prints flesch kincaid scores'''
        def average(numbers):
            avg = sum(numbers)/len(numbers)
            return avg
        scores = self.data[self.column].apply(lambda x : flesch_reading_ease(x))
        print("The average Flesch-Kincaid score for your text is {}".format(average(scores)))
        print("The max Flesch-Kincaid score for your text is {}".format(max(scores)))
        print("The min Flesch-Kincaid score for your text is {}".format(min(scores)))
    
    
    
    
    
    
    
    '''This function identifies and displays the top 10 most common bi-grams in the text data of the specified column. It then plots the results in a bar graph using the seaborn library.
    Parameters
    ----------
    None
    
    Returns
    -------
    A bar graph showing the top 10 most common bi-grams in the specified column of the data.'''
    def show_bi_grams(self):
        '''show most common bi-grams'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.column],2)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        plot = sns.barplot(x=y,y=x)
        return plot
    
    
    
    
    
    
    
    '''Show a bar graph of the most common bi-grams for two subsets of data.
    Parameters
    ----------
    split1: str or None (default is None)
        The label of the first subset of data to use. This value should match one of the unique labels in the 'split' column of the data.
    split2: str or None (default is None)
        The label of the second subset of data to use. This value should match one of the unique labels in the 'split' column of the data.

    Returns
    -------
    Displays a bar graph of the top 10 most common bi-grams for both subsets of data, showing the frequency of each bi-gram. Each bar graph is labeled with the name of the subset of data that it represents. The x-axis of each graph displays the bi-grams, while the y-axis displays their frequency.'''
    def show_bi_grams_split(self, split1=None, split2=None):
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split1][self.column],2)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        plt.bar(x,y)
        plt.title("Bi-Grams in {} data".format(str(split1)))
        plt.xticks(rotation=90, ha='right')
        plt.show
        
        '''shows a bar graph of most common bi-grams for train data'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split2][self.column],2)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        plt.bar(x,y)
        plt.title("Bi-Grams in {} data".format(str(split1)))
        plt.xticks(rotation=90, ha='right')
        plt.show
        
    
    
    
    
    
    
    '''Show output of the most common bi-grams for two subsets of data.
    Parameters
    ----------
    None

    Returns
    -------
    Output of the top 10 most common bi-grams for both subsets of data, showing the frequency of each bi-gram.'''
    def print_bi_grams(self):
        '''prints most common bi-grams'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.column],2)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        print("The most common bi-grams in your text are:")
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
            
    
    
    
    
    
    
    '''Show output of the most common bi-grams for two subsets of data.
    Parameters
    ----------
    split1: str or None (default is None)
        The label of the first subset of data to use. This value should match one of the unique labels in the 'split' column of the data.
    split2: str or None (default is None)
        The label of the second subset of data to use. This value should match one of the unique labels in the 'split' column of the data.

    Returns
    -------
    Output of the top 10 most common bi-grams for both subsets of data, showing the frequency of each bi-gram. Each bar graph is labeled with the name of the subset of data that it represents. The x-axis of each graph displays the bi-grams, while the y-axis displays their frequency.'''
    def print_bi_grams_split(self, split1=None, split2=None):
        '''prints most common bi-grams for train data'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split1][self.column],2)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        print("The most common bi-grams in your {} text are:".format(str(split1)))
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
        
        '''prints most common bi-grams for test data'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split2][self.column],2)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        print('\n')
        print("The most common bi-grams in your {} text are:".format(str(split2)))
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
        
        
    
    
    
    
    
    
    '''This function identifies and displays the top 10 most common tri-grams in the text data of the specified column. It then plots the results in a bar graph using the seaborn library.
    Parameters
    ----------
    None
    
    Returns
    -------
    A bar graph showing the top 10 most common tri-grams in the specified column of the data.'''
    def show_tri_grams(self):
        '''show most common tri-grams'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.column],3)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        plot = sns.barplot(x=y,y=x)
        return plot

    
    
    
    
    
    
    '''Show a bar graph of the most common tri-grams for two subsets of data.
    Parameters
    ----------
    split1: str or None (default is None)
        The label of the first subset of data to use. This value should match one of the unique labels in the 'split' column of the data.
    split2: str or None (default is None)
        The label of the second subset of data to use. This value should match one of the unique labels in the 'split' column of the data.

    Returns
    -------
    Displays a bar graph of the top 10 most common tri-grams for both subsets of data, showing the frequency of each tri-gram. Each bar graph is labeled with the name of the subset of data that it represents. The x-axis of each graph displays the tri-grams, while the y-axis displays their frequency.'''
    def show_tri_grams_split(self, split1=None, split2=None):
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split1][self.column],3)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        plt.bar(x,y)
        plt.title("Bi-Grams in {} data".format(str(split1)))
        plt.xticks(rotation=90, ha='right')
        plt.show
        
        #Reset for histogram 2
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split2][self.column],3)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        plt.bar(x,y)
        plt.title("Bi-Grams in {} data".format(str(split1)))
        plt.xticks(rotation=90, ha='right')
        plt.show

    
    
    
    
    
    
    '''Show output of the most common tri-grams for two subsets of data.
    Parameters
    ----------
    None

    Returns
    -------
    Output of the top 10 most common tri-grams for both subsets of data, showing the frequency of each tri-gram.'''
    def print_tri_grams(self):
        '''prints most common tri-grams'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.column],3)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        print("The most common tri-grams in your text are:")
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
            
            
            
            
            
    '''Show a bar graph of the most common tri-grams for two subsets of data.
    Parameters
    ----------
    split1: str or None (default is None)
        The label of the first subset of data to use. This value should match one of the unique labels in the 'split' column of the data.
    split2: str or None (default is None)
        The label of the second subset of data to use. This value should match one of the unique labels in the 'split' column of the data.

    Returns
    -------
    Output of the top 10 most common tri-grams for both subsets of data, showing the frequency of each tri-gram. Each bar graph is labeled with the name of the subset of data that it represents. The x-axis of each graph displays the tri-grams, while the y-axis displays their frequency.'''    
    def print_tri_grams_split(self, split1="train", split2="test"):
        '''prints most common tri-grams for train data'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split1][self.column],3)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        print("The most common bi-grams in your {} text are:".format(str(split1)))
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
        
        '''prints most common tri-grams for test data'''
        corpus=[]
        new=self.data[self.column].str.split()
        new=new.values.tolist()
        corpus=[word for i in new for word in i]
        def get_top_ngram(corpus, n=None):
            vec = CountVectorizer(ngram_range=(n, n)).fit(corpus)
            bag_of_words = vec.transform(corpus)
            sum_words = bag_of_words.sum(axis=0) 
            words_freq = [(word, sum_words[0, idx]) 
                          for word, idx in vec.vocabulary_.items()]
            words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
            return words_freq[:10]

        top_n_bigrams=get_top_ngram(self.data[self.data[self.split]==split2][self.column],3)[:10]
        x,y=map(list,zip(*top_n_bigrams))
        print('\n')
        print("The most common tri-grams in your {} text are:".format(str(split2)))
        for word, count in zip(x,y):
            print(str(word) + " : " + str(count))
    
    
    
    
    
    

    '''Creates a topic model visualization using Latent Dirichlet Allocation (LDA) algorithm, which identifies topics in a set of documents and assigns each word in a document to one of the identified topics. 
    Parameters
    ----------
    topics: Number of topics you want to see in your topic model (Default: 10)

    Returns
    -------
    A graph containing the topic model visualization.
    '''
    def topic_model(self, topics=10):
        model_data = self.data['text_without_stopwords'].values.tolist()
        model_data = [m.split(' ') for m in model_data]
        id2word = Dictionary(model_data)
        corpus = [id2word.doc2bow(text) for text in model_data]
        
        lda_model = LdaModel(corpus=corpus,
                   id2word=id2word,
                   num_topics=topics,
                   random_state=0,
                   chunksize=100,
                   alpha='auto',
                   per_word_topics=True)
        doc_lda = lda_model[corpus]
        #Creating Topic Distance Visualization 
        pyLDAvis.enable_notebook()
        graph = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
        return graph
    
    
    
    
    
    
    '''Creates a histogram of cosine similarity between all pairs of vectors in the input list.
    Parameters:
    --------
    vectors- DataFrame column containing word vectors

    returns:
    --------
    histogram showing cosine similarities'''
    def show_cosine_sim(self, vectors=None):
        n = len(self.data[vectors])
        #Create blank list the same size as our vectors
        cosine_sims = np.zeros((n, n))

        # Compute pairwise cosine similarities
        for i in range(n):
            for j in range(i+1, n):
                cosine_sims[i, j] = cosine_similarity(self.data[vectors][i].reshape(1, -1), self.data[vectors][j].reshape(1, -1))[0, 0]
                cosine_sims[j, i] = cosine_sims[i, j]

        # Plot histogram of cosine similarities
        plt.hist(cosine_sims)
        plt.xlabel('Cosine similarity')
        plt.ylabel('Frequency')
        plt.title('Histogram of cosine similarity')
        plt.show()
        
      
    
   
    
    
        '''Uses KNN to find outliers in a list of vectors.
    Parameters:
    --------
    vectors (list): A list of 1D numpy arrays representing vectors.
    k (int): The number of nearest neighbors to consider for each vector. Defaults to 5.
    threshold (float): The threshold for determining outliers based on the median distance to k-nearest neighbors. Defaults to 3.0.

    Returns:
    --------
    A list of the indices of the outlier vectors in the input list.'''
    def find_outliers_knn(self, vectors=None, k=5, threshold=3.0):
        nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(self.data[vectors].tolist())
        distances, indices = nbrs.kneighbors(self.data[vectors].tolist())
        median_distances = np.median(distances, axis=1)
        outlier_indices = np.where(median_distances > threshold * np.median(median_distances))[0]
        ind_list =  outlier_indices.tolist()
        print("The following vectors are outliers:")
        for ind in ind_list:
            print(self.data.loc[ind])

            

class vizzy_token:
    '''A class for visualizing token frequencies in text data.
    Parameters
    ----------
    dataframe: pandas DataFrame
        A pandas DataFrame containing the text data to be visualized.
    text: str
        The name of the column in `dataframe` that contains the text data.
    split: str or None, optional (default=None)
        The name of a column in `dataframe` that contains labels for the data splits, 
        or None if the data is not split.
    labels: list or None, optional (default=None)
        A list of labels for the data splits, in the order that they appear in the `split` column. '''
    def __init__(self, dataframe, text, split = None, labels = None):
        self.data = dataframe
        self.text = text
        self.split = split
        self.labels = labels
    
    
    
    
    
    '''Plots a histogram of the counts for each label in the specified column.
    Parameters
    ----------
    column : str
        The name of the column to plot the histogram for.

    Returns
    -------
    Histogram of the counts for each label in specified column'''
    def show_labels_count(self, column):
        plt.hist(self.data[column])
        plt.title('Histogram of {}'.format(column))
        plt.show()
        
    
    
    
    
    
    
    '''Show the count of each label, split by a given column (if provided). This method generates a bar plot of the count of each label, split by a given column (if provided). The splits parameter allows the user to specify a list of column names to split the data by. The method checks if the split column and label columns are the same and raises a ValueError if they are. If no split is specified, the method will generate the plot for the entire dataset.
    Parameters:
    -----------
    splits: list, default None
        A list of column names to split the data by. The count of labels will be shown for each split.

    Returns:
    --------
    None'''
    def show_labels_count_split(self, splits=None):
        '''show count of each label'''
        if self.split != None:
            for l in self.labels:
                for s in splits:
                    if l == self.split:
                        raise ValueError("Your split column and label columns are the same. Please try again.")
                    labels = self.data[self.data[self.split]==s][l]
                    counter = Counter(labels)
                    x = list(counter.keys())
                    y = list(counter.values())
                    sorted_y, sorted_x = zip(*sorted(zip(y, x), reverse=True))
                    plt.bar(sorted_x, sorted_y)
                    plt.title("{} by {}".format(s,l))
                    plt.xticks(rotation=90, ha='right')
                    plt.show()
        else:
            for l in self.labels:
                labels = self.data[l]
                counter = Counter(labels)
                x = list(counter.keys())
                y = list(counter.values())
                sorted_y, sorted_x = zip(*sorted(zip(y, x), reverse=True))
                plt.bar(sorted_x, sorted_y)
                plt.xticks(rotation=90, ha='right')
                plt.show()

    
    
    
    
      
    '''Prints the count of uppercase letters, lowercase letters and integers in the given column.
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    def print_case(self):
        def count_upper_lower_integer(df, column):
            upper = 0
            lower = 0
            integer = 0
            for token in df[column]:
                if isinstance(token, int):
                    integer += 1
                elif isinstance(token, str):
                    if token.islower():
                        lower += 1
                    elif token.isupper():
                        upper += 1
            return {'upper': upper, 'lower': lower, 'integer': integer}
        result = count_upper_lower_integer(self.data, self.text)
        print(result)
        
        
        
        
        
        
        
    '''Displays a bar graph showing the count of upper case, lower case, and integer tokens in a given column of the dataset.
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    def show_case(self):
        def count_upper_lower_integer(df, column):
            upper = 0
            lower = 0
            integer = 0
            for token in df[column]:
                if isinstance(token, int):
                    integer += 1
                elif isinstance(token, str):
                    if token.islower():
                        lower += 1
                    elif token.isupper():
                        upper += 1
            return {'upper': upper, 'lower': lower, 'integer': integer}
        result = count_upper_lower_integer(self.data, self.text)
        keys = []
        items = []
        for key, item in result.items():
            keys.append(key)
            items.append(item)
        plt.bar(keys, items)
        plt.title('Tokens by case')
        plt.show

class vizzy_doc:
    '''A class for visualizing data in text documents. 
    
    Parameters:
    -----------
    data : pandas.DataFrame
        The dataframe to use for visualization.
        
    column1 : str
        The first column to use for analysis.
        
    column2 : str, optional
        The second column to use for analysis.
        
    column3 : str, optional
        The third column to use for analysis.
        
    column4 : str, optional
        The fourth column to use for analysis.
        
    column5 : str, optional
        The fifth column to use for analysis.
        
    date_column : str, optional
        The name of the column containing date information.
        
    date_format : str, optional
        The format of the date information in the date column.
        
    split : str, optional
        The name of the column to use for splitting the data.'''
    def __init__(self, data, column1, column2=None, column3=None, column4=None, column5=None, date_column=None, date_format=None, split=None):
        self.data = data
        self.column1 = column1
        self.column2 = column2
        self.column3 = column3
        self.column4 = column4
        self.column5 = column5
        self.date_column = date_column
        self.date_format = date_format
        self.split = split
        self.set = [column1, column2, column3, column4, column5]
        
        
        
        
        
        
        
    '''This function prints the number of unique documents and the number of unique values in the specified columns 
    of your dataset. The count of each column will only be printed if it is provided during the initialization 
    of the vizzy_doc object.

    Parameters
    ----------
    None

    Returns
    -------
    None'''
    def print_doc_stats(self):
        '''Print the statistics of your document'''
        def counter(data, column):
            return data[column].nunique()
        docs = max(idx for idx, other in self.data.iterrows())
        print("Here is your data summary:")
        print("Total number of documents: {}".format(docs))
        print("Total number of {}: {}".format(str(self.column1), (counter(self.data, self.column1))))
        if self.column2 != None:
            print("Total number of {}: {}".format(str(self.column2), (counter(self.data, self.column2))))
        else:
            pass
        if self.column3 != None:
             print("Total number of {}: {}".format(str(self.column3), (counter(self.data, self.column3))))
        else:
            pass
        if self.column4 != None:
             print("Total number of {}: {}".format(str(self.column4), (counter(self.data, self.column4))))
        else:
            pass
        if self.column5 != None:
             print("Total number of {}: {}".format(str(self.column5), (counter(self.data, self.column5))))
        else:
            pass                
    
    
    
    
    
    
    
    '''This function displays the statistics of your document. The visualizations include a bar graph for the counts
    of each unique value for the specified columns.
    Parameters
    ----------
    None

    Returns
    -------
    A set of bar graphs for each specified column will be shown.'''
    def show_doc_stats(self):
        if self.date_column != None and self.date_format != None:
            def extract_year(data, column, date_format=self.date_format, new_column=None):
                # Extract the year from the date column
                data[new_column] = pd.to_datetime(data[column], format = date_format).dt.year
                return data
            df = extract_year(self.data, self.date_column, date_format=self.date_format, new_column='year')
            year_counts = df['year'].value_counts()
            year_percents = year_counts / year_counts.sum() * 100
            plt.figure(0)
            plt.bar(year_counts.index, year_counts)
            plt.title("Docs by {}".format(str(self.date_column)))
        else:
            pass
        
        if self.column2 != None:
            col2_counts = self.data[self.column2].value_counts()
            col2_percents = col2_counts/col2_counts.sum() * 100
            plt.figure(1)
            plt.bar(col2_counts.index, col2_counts)
            plt.title("Docs by {}".format(str(self.column2)))
        else:
            pass
            
        if self.column3 != None:
            col3_counts = self.data[self.column3].value_counts()
            col3_percents = col3_counts/col3_counts.sum() * 100 
            plt.figure(2)
            plt.bar(col3_counts.index, col3_counts)
            plt.title("Docs by {}".format(str(self.column3)))
        else:
            pass
        
        if self.column4 != None:
            col4_counts = self.data[self.column4].value_counts()
            col4_percents = col4_counts/col4_counts.sum() * 100 
            plt.figure(3)
            plt.bar(col4_counts.index, col4_counts)
            plt.title("Docs by {}".format(str(self.column4)))
        else:
            pass
        
        if self.column5 != None:
            col5_counts = self.data[self.column5].value_counts()
            col5_percents = col5_counts/col5_counts.sum() * 100 
            plt.figure(4)
            plt.bar(col5_counts.index, col5_counts)
            plt.title("Docs by {}".format(str(self.column5)))
        else:
            pass
        
        plt.show()
        
        
        
        
        
        
    
    '''Plots histograms of the specified categorical variables, comparing the distributions of the specified
    splits.

    Parameters:
    --------
    split1 (str): the name of the first split to compare
    split2 (str): the name of the second split to compare

    Returns:
    --------
    Histograms of specified variables'''    
    def show_split_doc_stats(self, split1=None, split2=None):
        if self.date_column != None and self.date_format != None:
            def extract_year(data, column, date_format=self.date_format, new_column=None):
                # Extract the year from the date column
                data[new_column] = pd.to_datetime(data[column], format = date_format).dt.year
                return data
            self.data = extract_year(self.data, self.date_column, date_format=self.date_format, new_column='year')
            self.set.append("year")
        else:
            pass
        # Get the list of categorical variables
        categorical_vars = [col for col in self.set if col != None]

        # Loop through each categorical variable
        for var in categorical_vars:
            # Plot the histogram for all values
            plt.hist(self.data[var], bins=20, color='blue', alpha=0.5, label='All')

            # Plot the histogram for train values
            plt.hist((self.data[var][self.data[self.split]==split1]), bins=20, color='green', alpha=0.5, label=str(split1))

            # Plot the histogram for test values
            plt.hist((self.data[var][self.data[self.split]==split2]), bins=20, color='red', alpha=0.5, label=str(split2))
            
            # Add the labels and title
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.title('Histograms of {}'.format(str(var)))

            # Show the legend
            plt.legend()

            # Show the plot
            plt.show()