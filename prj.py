from collections import Counter
import os
import pprint
import sys


review = []
positive_reviews = []
negative_reviews = []
"""
Say for instance we have a review saying: "This is a good movie"
P(bad| review) = P( bad | "good") * P( bad| "movie")
*Assume "this", "is", "a" is filtered out.

"""
def sentiment(review, counts):
	bayes = float(1)
	#Calculate the good
	for word in review.split():
		num_of_reviews = float(len(counts))
		num_of_word_occur = float(counts[word.lower()])
		#print num_of_word_occur
		probability =  float(num_of_word_occur / num_of_reviews)
		if(probability == float(0)):
			probability = 1
		bayes *= probability
		#print bayes
	return bayes

def naivebayes(data, reviewtype=None):
	review.append(data)
	if reviewtype is None:
		print('Nice try, brown!')
		return

	elif reviewtype is 'positive':
		positive_reviews.append((data, '+'))

	elif reviewtype is 'negative':
		negative_reviews.append((data, '-'))



def main(argv):

	if len(sys.argv) != 3:
		sys.exit('Usage: %s <positive reviews> <negative reviews>' % sys.argv[0])

	pos = sys.argv[1]
	neg = sys.argv[2]


	for root, dirs, files, in os.walk(pos, topdown=True):
		for review in files:
			# we'll need to feed these each into naive bayes
			# naivebayes(review, positive)
			filename = os.path.join(root, review)
			#print(os.path.join(root, review))
			#print(filename)
			text = open(filename, 'r')
			text = text.read()
			text = text.replace('<br />', '')
			# Reduce data redundancy such as: 'not,', 'actor;', 
			text = text.replace('...', ' ')
			text = text.replace(';', ' ')
			text = text.replace(',', ' ')
			text = text.replace('-', ' ')
			text = text.replace('.', ' ')
			#print(text)
			naivebayes(text, 'positive')


	print('read and processed positive reviews\n')



	for root, dirs, files, in os.walk(neg, topdown=True):
		for review in files:
			# we'll need to feed these each into naive bayes
			# naivebayes(review, negative)
			filename = os.path.join(root, review)
			#print(os.path.join(root, review))
			#print(filename)
			text = open(filename, 'r')
			text = text.read()
			text = text.replace('<br />', '')
			# Reduce data redundancy such as: 'not,', 'actor;', 
			text = text.replace('...', ' ')
			text = text.replace(';', ' ')
			text = text.replace(',', ' ')
			text = text.replace('-', ' ')
			text = text.replace('.', ' ')
			#print(text)
			naivebayes(text, 'negative')


	print('read and processed negative reviews\n')
	# Statistics:
	num_of_positive_reviews = float(len(positive_reviews))
	num_of_negative_reviews = float(len(negative_reviews))
	num_of_total_reviews    = num_of_positive_reviews + num_of_negative_reviews
	print "# of positive review : %s\n" % num_of_positive_reviews
	print "# of negative review : %s\n" % num_of_negative_reviews
	print "# of total review    : %s\n" % num_of_total_reviews
	print "positive probability : %s\n" % float(num_of_positive_reviews / num_of_total_reviews)
	print "positive probability : %s\n" % float(num_of_negative_reviews / num_of_total_reviews)

	clean = []
	for (text, review) in positive_reviews:
		cleanup = [word.lower() for word in text.split() if len(word) > 2]
		clean.append((cleanup, review))

	#pprint.pprint(clean)

	tmp = []
	for (txt, rev) in clean:
		tmp.extend(txt)

	pos_counts = Counter(tmp)
	# Not recommended to pprint for mass data
	#pprint.pprint(pos_counts)
	


	#print('\n\n\n--> done processing positive counts')
	clean = []
	for (text, review) in negative_reviews:
		cleanup = [word.lower() for word in text.split() if len(word) > 2]
		clean.append((cleanup, review))


	tmp = []
	for (txt, rev) in clean:
		tmp.extend(txt)

	neg_counts = Counter(tmp)
	# Not recommended to pprint for mass data
	#pprint.pprint(neg_counts)

	#print('\n\n\n--> done processing negative counts')



	text_to_review = raw_input('Input a review to be rated: ')
	positive_bayes = sentiment(text_to_review, pos_counts)
	negative_bayes = sentiment(text_to_review, neg_counts)
	print "positive bayes = %s" % positive_bayes
	print "negative bayes = %s" % negative_bayes
	if(positive_bayes > negative_bayes):
		print "Review is positive review"
	else:
		print "Review is negative review"

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))