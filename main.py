import json
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches

## CONSTANTS

DOCUMENT_PATH = "./data/doc1.json"


## Args for CLI


def parser_function() -> argparse.Namespace:
    """
    Parse the arguments for the CLI
    """
    parser = argparse.ArgumentParser(description="Process the document")
    parser.add_argument(
        "-d",
        "--document",
        type=str,
        help="Path to the document to process",
        default=DOCUMENT_PATH,
    )

    parser.add_argument(
        "-v",
        "--visualize",
        help="Visualize the document",
        default=False,
        action="store_true",
    )
    return parser.parse_args()


## Loader function


def load_document(path: str) -> dict:
    """
    Load the document from the json file
    """
    f = open(path, "r")
    data = json.load(f)
    return data


## Question 1 : Simple heuristic to detect names

# Use as heuristic for capitalization of words to determine if they are potential names

# Would be even better to do a lookup in a dictionary of names to see if it is a name
# or as names can be invented or derived, use a dictionnary of common words and get
# the words that are not in the dictionary as potential names


# Add function to visualize the input data


def visualize_page(data: dict, page_number: int) -> None:
    """
    Visualize one page of a document with the bounding boxes
    from the json file
    """

    fig, ax = plt.subplots()
    page = data["pages"][page_number]
    for word in page["words"]:
        x_min = word["bbox"]["x_min"]
        x_max = word["bbox"]["x_max"]
        y_min = word["bbox"]["y_min"]
        y_max = word["bbox"]["y_max"]
        pc = patches.Rectangle(
            (x_min, y_min),
            x_max - x_min,
            y_max - y_min,
            fill=False,
            edgecolor="red",
        )
        ax.add_patch(pc)
        plt.text(x_min, y_min, word["text"], fontsize=12)
    plt.show()


def heuristic_capitalization(word: str) -> bool:
    """
    Check if the 1st letter of the word is capitalized
    """
    return word[0].isupper()


def search_for_names(data: dict) -> list:
    """
    Search for names in the json file
    """
    capitalized_words = []
    for page in data["pages"]:
        for word in page["words"]:
            if heuristic_capitalization(word["text"]):
                capitalized_words.append(word["text"])
    return capitalized_words


if __name__ == "__main__":
    # Parse the arguments
    args = parser_function()

    path = args.document
    visualize = args.visualize

    # Load the document
    data = load_document(path)

    # CLI
    if visualize:
        visualize_page(data, 0)

    print("Searching for names")
    names = search_for_names(data)
    print("Potential names found: ", names)
