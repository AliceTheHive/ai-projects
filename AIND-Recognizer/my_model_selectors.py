import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=20,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states, X=self.X, lengths=self.lengths):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object

        Calculate the bic_score for models of different component lengths, finally return with model with the highest BIC score 
        
        # BIC = −2 log L + p log N
        # L = is the likelihood of the model
        # p = is the number of parameters
        # N = is the number of data points

        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        bic_scores = []
        try:
            for n in self.n_components:

                model = self.base_model(n)
                log_l = model.score(self.X, self.lengths)
                p = n ** 2 + 2 * n * model.n_features - 1
                bic_score = -2 * log_l + p * math.log(n)
                bic_scores.append(bic_score)
        except Exception as e:
            pass

        if bic_scores:
            best_state = self.n_components[np.argmin(bic_scores)] 
        else:
            best_state = self.n_constant
        return self.base_model(best_state)


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))

    My Notes:
    SUM(log(P(X(all but i) : sum all the log_l except the log_l of the current model
    1/(M-1) : divide by the number of models
    log(P(X(i)) log_l of the current model

    Putting it all together:
    log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))

    I guess you are trying to find the greatest difference between  the target model and other models,
    so you are trying to maximum the difference between the log likelihoods.


    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        dic_scores = []
        logs_l = []
        try:
            for n_component in self.n_components: #iterate through all the state numbers
                model = self.base_model(n_component) #create the model
                logs_l.append(model.score(self.X, self.lengths)) #score the model and add to list
            sum_logs_l = sum(logs_l) #sum up all the log likelihoods calculated
            m = len(self.n_components) #total number of models
            for log_l in logs_l:
                dic_score = log_l - (1 / (m - 1)) * (sum_logs_l - log_l) 
                dic_scores.append(dic_score)
        except Exception as e:
            pass

        if dic_scores:
            best_state = self.n_components[np.argmax(dic_scores)]
        else:
            best_state = self.n_constant
        return self.base_model(best_state)


class SelectorCV(ModelSelector):
    ''' select best model based on average log likelihood of cross-validation folds 

    We want to split the data set into k units, with one of the units being test and k-1 being train.  
    Train the model multiple times with a different unit being the test set each time.  Take the mean of the result.  
    This will give us a mucher more accurate model performance with less risk of overfitting.
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        mean_scores = []
        split_method = KFold(4)

        try:
            for n_component in self.n_components:
                
                kfold_scores = []
                for train_idx, test_idx in split_method.split(self.sequences):
                    # combine training indices with sequences to prepare training data for model
                    train_X, train_length = combine_sequences(train_idx, self.sequences)
                    # train model with trainign data.
                    model = self.base_model(n_component, train_X, train_length)
                    # combine test indices with sequences to prepare test data for model
                    test_X, test_length = combine_sequences(test_idx, self.sequences)
                    # run the model and score on the test set
                    test_score = model.score(test_X, test_length)
                    kfold_scores.append(test_score)
                # finally, compute mean of all fold scores
                mean_scores.append(np.mean(kfold_scores))
        except Exception as e:
            pass

        if mean_scores:
            best_state = self.n_components[np.argmax(dic_scores)]
        else:
            best_state = self.n_constant
        return self.base_model(best_state)
