## Machine Learning Engineer Challenge Lifen 2023

### Goals

We are trying to predict the patient's first and last names for a given medical report.

### Dataset

Let's imagine we have a dataset with 100k unlabeled documents medical documents. See below 3 examples:

![docs](https://user-images.githubusercontent.com/51329768/253037781-0d834349-9da9-47e9-8108-4cf62912c229.png)

For each document we have a json representation that gives us absolute coordinates for each word, for exemple:

```json
{
  "pages": [
    {
      "words": [
        {
          "text": "hanche",
          "bbox": { "x_min": 0.75, "x_max": 0.81, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "JACQUES",
          "bbox": { "x_min": 0.74, "x_max": 0.83, "y_min": 0.16, "y_max": 0.17 }
        },
        {
          "text": "pour",
          "bbox": { "x_min": 0.57, "x_max": 0.61, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "la",
          "bbox": { "x_min": 0.73, "x_max": 0.75, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "en",
          "bbox": { "x_min": 0.23, "x_max": 0.26, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "bien",
          "bbox": { "x_min": 0.15, "x_max": 0.19, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "consultation",
          "bbox": { "x_min": 0.26, "x_max": 0.36, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "Monsieur",
          "bbox": { "x_min": 0.36, "x_max": 0.44, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "Jean",
          "bbox": { "x_min": 0.44, "x_max": 0.48, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "à",
          "bbox": { "x_min": 0.72, "x_max": 0.73, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "droite.",
          "bbox": { "x_min": 0.82, "x_max": 0.87, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "revu",
          "bbox": { "x_min": 0.19, "x_max": 0.23, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "DUPONT",
          "bbox": { "x_min": 0.49, "x_max": 0.57, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "douleur",
          "bbox": { "x_min": 0.65, "x_max": 0.71, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "J’ai",
          "bbox": { "x_min": 0.12, "x_max": 0.15, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "une",
          "bbox": { "x_min": 0.61, "x_max": 0.65, "y_min": 0.09, "y_max": 0.1 }
        },
        {
          "text": "Nicolas",
          "bbox": { "x_min": 0.67, "x_max": 0.73, "y_min": 0.16, "y_max": 0.17 }
        },
        {
          "text": "Docteur",
          "bbox": { "x_min": 0.6, "x_max": 0.67, "y_min": 0.16, "y_max": 0.17 }
        }
      ]
    }
  ],
  "original_page_count": 1,
  "needs_ocr_case": "no_ocr"
}
```

We have the target outputs: first and last names and we want to be able to predict them automatically for each new document.

### Questions

We are going to study 3 different approaches (which you are obviously not going to implement for this challenge):

1. The simplest heuristic you can think of (no ML). So simple it is not required to handle all 3 examples above.
2. ML pipeline fully in-house, a solution that should achieve high accuracy, fast and cost-efficient during inference (millions of real-time predictions per week).
   - What do you need to build this solution?
   - What's your process for building this algorithm?
   - What kind of algorithms do you want to try? (You may talk about different approaches and talk about pros & cons)
   - What features would you engineer (if any)?
   - Think of edge cases (complicated or ambiguous docs: we are deployed in more than 700 healthcare organisations and people sometimes get very creative) and how you would handle them.
3. ML solution using an external API (LLMs).
   - How would you leverage this kind of model to solve this problem?
   - What is the advantage and disadvantage of this approach compared to the previous one?

What if instead of those two targets we want to structure 300 different fields (many medical variables like weight, medications taken, medical history, ....) in these documents? How would you approach this problem?

### Deliverables

We expect the following deliverables:

- **A small python github repo** containing the solution for the 1st approach. We are mostly using this part to evaluate your Software Engineering skills and discuss best practices. The actual quantity of code expected is _very small_, but do not hesitate to setup your solution with all the best Software Engineering practices you know. It may be small webserver with one route which takes a document as input and returns the predicted first and last names, but could be just a python script, or a CLI. Don't hesitate to list ideas for improvements in the README instead of spending too much time on a perfect solution.
- **A 30 min presentation-discussion** of your ideas for solutions 2 and 3. You can prepare a doc with bullet points or slides. The goal here is mostly to evaluate your data science skills. Focus on content over form
