from collections import Counter
import os
import pprint
import sys



positive_reviews = []
negative_reviews = []

def naivebayes(data, reviewtype=None):
	if reviewtype is None:
		print('Nice try, brown!')
		return

	elif reviewtype is 'positive':
		positive_reviews.append((data, '+'))





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
			print(filename)
			text = open(filename, 'r')
			text = text.read()
			text = text.replace('<br />', '')
			#print(text)
			naivebayes(text, 'positive')


	print('read and processed positive reviews\n')



	for root, dirs, files, in os.walk(neg, topdown=True):
		for review in files:
			# we'll need to feed these each into naive bayes
			# naivebayes(review, negative)
			print(os.path.join(root, review))


	print('read and processed negative reviews\n')

	clean = []
	for (text, review) in positive_reviews:
		cleanup = [word.lower() for word in text.split() if len(word) > 2]
		clean.append((cleanup, review))

	#pprint.pprint(clean)

	blah = []
	for (derp, rev) in clean:
		blah.extend(derp)

	a = Counter(blah)
	pprint.pprint(a)

	#text_to_review = raw_input('Input a review to be rated: ')
	#sentiment = naivebayes(text_to_review, None)

	#pprint.pprint(positive_reviews)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))