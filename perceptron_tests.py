import nose.tools as nt
from perceptron import Perceptron

def no_training_data_supplied_test():
	the_preceptron = Perceptron()
	result = the_preceptron.predict()
	nt.assert_equal(result, None, 'Should have no result with no training data.')