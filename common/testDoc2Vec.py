import gensim.models as genModel
import tweetPrepocessing
import databaseFunctions

class LabeledLineSentence(object):
    def __init__(self, doc_list):
        self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
              yield genModel.doc2vec.LabeledSentence(doc, ['TWEET_%s' % idx])

def build_model(tweets):
    it = LabeledLineSentence(tweets)
    model = genModel.Doc2Vec(size=300, window=5, min_count=2,
                             dm=1, dbow_words=1, dm_concat=1,
                             alpha= 0.025, min_alpha=0.025)
    return it, model

def train_model(it,model, tweets):

    model.build_vocab(it)
    for epoch in range(5):
        print 'iteration ' + str(epoch + 1)
        model.train(it, total_examples=len(tweets), epochs=1)
        model.alpha -= 0.002
        model.min_alpha = model.alpha

    #model.train(it, total_examples=len(tweets), epochs=50)
    return model

def main(tweets):
    iterator, model = build_model(tweets)
    print("Model Built")
    model = train_model(iterator, model, tweets)
    model.save('OffensiveWords.doc2vec')
    print ("Model saved")
    return model

if __name__ == '__main__':
    obj = databaseFunctions.DatabaseFunction('abc')
    df = obj.getSQLData()
    df = tweetPrepocessing.getCleanTweets(df)
    tweets = list(df['tweet'])
    model = main(tweets)