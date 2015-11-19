import sys
import os




def naivebayes(data, reviewtype=None):
	if reviewtype = None:
		print('Nice try, brown!')
	return


def main(argv):

	if len(sys.argv) != 3:
		sys.exit('Usage: %s <positive reviews> <negative reviews>' % sys.argv[0])

	pos = sys.argv[1]
	neg = sys.argv[2]


	for root, dirs, files, in os.walk(pos, topdown=True):
		for review in files:
			# we'll need to feed these each into naive bayes
			# naivebayes(review, positive)
			print(os.path.join(root, review))


	print('read and processed positive reviews')



	for root, dirs, files, in os.walk(neg, topdown=True):
		for review in files:
			# we'll need to feed these each into naive bayes
			# naivebayes(review, positive)
			print(os.path.join(root, review))


	print('read and processed negative reviews')


	text_to_review = raw_input('Input a review to be rated: ')
	sentiment = naivebayes(data, None)



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))