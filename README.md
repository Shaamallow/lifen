# README

## Introduction

Lifen Take Home Assignment for Machine Learning Engineer position (summer 2024)
Find the assignment in `/docs` folder.

## Folder Structure

```bash
.
├── data
│   └── doc1.json
├── docs
│   └── questions.md
├── environment.yml
├── main.py
└── README.md
```

## Requirements

Install requirements using the `requirements.txt` file. (I advised to use a python version manager such as conda or mamba and use Python 3.10)

```bash
pip install -r requirements.txt
```

## Running the code

Run the `main.py` script as a CLI to see the results. The script can take 2 arguments (input path and visualization), use the `--help` flag to see the options.

```bash
python main.py -d data/doc1.json -v
```

## Improvements

The heuristic is one of the simplest and doesn't allow to distinguish in between capitalized words at the beginning of a sentence and the real names. Also the doctor is not distinguish from the patient. A simple yet naive approach would be to use a dictionary of names and check for matching words. As advised, as names can be quite diverse and have a lot of variations, we could use a dictionary of _non-names_ and check for the remaining words. This would be effective but would cost a lot on memory for a large vocabulary dataset (ex : Glove Twitter Dataset used for training is already 1.2M words..) and the dictionary would have to be updated regularly.

For a better user experience, we could create a gradio interface to upload pdf files using a simple drag and drop, then visualize the results of the OCR model turning it into a json and then the output of the heuristic and the script. But this is already overkill for the current task as we only have 1 document and no OCR model here. Hence a CLI approach.
