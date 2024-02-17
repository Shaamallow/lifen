# Question 2

Setup the solution :

1. Design the solution to handle the workload.

- Input : json document in the format provided
- Output : First Name; Last Name of the Patient

2. Necessary structure :

- Document API endpoint to receive the pdf
- Preprocessing of the document : OCR to extract to the json format
- Add metadata to the input (might be useful for the features later on)
- Add queue to handle multiple requests at one (expecting multiple users on 1 endpoint)
- Add a database to store the output data
- Add a logging system to track the requests and help monitor

Usual NLP preprocessing steps :

- Map words to dictionary
- Remove stop words (definitely not potential names, only useful for the from scratch Classifier, we should keep it for the transformer model)
- Tokenization : Would be interesting to have a representation of the words in a latent space and good feature for the classification.

3. Algorithm :

- Assuming we have an annotated dataset, we can train a classifier to identify the names in the document using as a input the following features.

We could also use a pre-trained model to identify the names in the document using an out-of-the-box solution such as Spacy and filter for only names. While we might want to use the output of the NER model as a feature for our classifier, it is not very efficient as we are already using a Tokenizer in our features list and it would be redundant. And we are also not choosing between the patient and the doctor.

Using a simple dense layer :

- Treat each word by itself with its features and classifier it. Efficient but lack the awareness of the context of the words around and the document.

Use a recurrent neural network :

Allow to have a better understanding of the context of the words. More efficient but still lacks the understanding of the document as a whole and it's slow to train.

Use a transformer model :

- Allow to have a better understanding of the document as a whole. Most efficient but also most costly.

Either add the new features as new embeddings or use them only as features for the classifier.

- Embeddings : Need to redo the training for this, it's a costly solution but could help getter a better understanding of the layout of the document
- Final Classification layer : lower cost but probably less accurate. Still need to train the end layer.

For the 2 last solutions, we need to turn the json into a sequence of words, we can use the bbox position to go line by line and from left to right.

4. Features :

- Train/Use an Tokenizer using a given medical dataset (or a general dataset if none available) to have a latent space representation of the words as common nouns would have a specific representation we can use to identify proper nouns. We could use Glove and (or not) fine tune it on a medical dataset. : High cost feature but would be an accurate representation of the words.
- Use the bbox position as the name of the doctor is more likely to be at a specific position in the document (signature, stamp, etc..) : low cost feature
- Capitalized words are more likely to be proper nouns : low cost feature
- Fully capitalized words (more likely to be acronyms and last names) : low cost feature

5. Edge cases :

For specific document layout, the text might be difficult to turn into a proper sequence of words. We need to check for big separation between paragraphs, columns and blocks of text. We can use a tree structure to represent the text and use the bbox position to identify the different blocks of text and a distance threshold to identify the different paragraphs.
When no names are detected, store the document to be reviewed by a human and add it to the training set.
