import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]


   Description:
   models contains HMM Gaussian models for each word
   test_set contains features and label for test set

   probabilities: probabilities for each word using the best model.
   guesses: the word that ends up being predicted for each sequence.


  double for loop.  For each word in the test set, you want to iterate through all the models for each word and 
  calculate the log_l based on the sequence from that test set.  Then you want to take the max log_l out of all models, 
  which ends up being your prediction

   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []

    X_lengths = test_set.get_all_Xlengths() #get all the sequences and lengths from the test set
    for X, lengths in X_lengths.values(): #iterate through all the word sequences in the test set

        max_score = float("-inf") # Save max score as recognizer iterates the list
        best_guess = None # Save best guess as recognizer iterates the list
        for word, model in models.items(): #iterate through all word models
            try:
                myscore = model.score(X, lengths) # Score word using model
                
                #keep track of the best score
                if myscore > max_score:
                    max_score = myscore
                    best_guess = word          
            except:
                pass

        #append the best guess to the list
        guesses.append(best_guess)

        #append the log loglihood
        log_like = {}
        log_like[word] = max_score
        probabilities.append(log_like)

    return probabilities, guesses
