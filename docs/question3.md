# Question 3

1. Leverage an LLM for this task

- API endpoint to receive the pdf
- OCR model to extract the text
- Transform the json into a sequence of words with the bbox position and create paragraphs in case of big separation (same method as for question 2)
- Send the sequence of words to the LLM and ask it to filter for names with the prompt

2. Advantages / Disadvantages

- **Very expensive** method as API calls are costly if we send the entire document. We could do filter before hand.
- Can't train or fine-tune the model on a medical dataset if it's proprietary
- Probably a **better accuracy** than the other 2 solutions
- Not possible to add hard constraint to generate consistent output
- External dependency (low maintenance but vulnerability)
- Privacy concerns (especially for medical data...)

## Question 4

If we have 300 different fields, the former classification method is not reliable as it's quite difficult to have a consistent model for many classes.Also, it wouldn't scale well and we would have to create a new model if we add a new field to classify. Thus it's better to use a generative model that is capable of 0-shot classification tasks. We would still need to work on how to make sure the output format is the right one but it's an other task.
