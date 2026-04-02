# All you need to know about vector DB

- **Repo_Name:** `learn-by-rebuilding`
- **Category:** `vector-embedding-store`
- **Project:** `all-you-need-to-know-vector-db`
- **Project Root Path:** `learn-by-rebuilding/vector-embedding-store/all-you-need-to-know-vector-db`

## Article Used
[All you need to know about vector DB](https://towardsdatascience.com/all-you-need-to-know-about-vector-databases-and-how-to-use-them-to-augment-your-llm-apps-596f39adfedb/)

## Overview
This project re-implements and experiments with the concepts presented in the article mentioned above.  

The goal is to discover and harness the power of vector databases. 

---

## Objectives

- How to convert from a text to embeddings?
- After getting high dimentional vector embedding, applying PCA and plotting in 2D.
- Distance calculation and Cosine similarity among pairs of texts
- How to store the vector embeddings in a vector database?
- After storing the embeddings in a vector store, how to query it?

---

## Project Structure

Here is the directory structure:
```
data-extraction/docling-document-alchemist/
├── readme.md
├── .gitignore
├── implementation.ipynb
├── experiments.ipynb
└── requirements.txt
```

---

## Description of Code files

- `implementation.ipynb`: In this notebook I tried to re-implement the exact process as much as possible shown in the article. I have documented the results I found. There were few issues in the implementation, I fixed those. I also documented some of my reviews and comments. 
- [***] `experiments.ipynb`: In this notebook I did few more relavant experiments. 

## How to run?

- Create one venv using `python -m venv .mlenv` command in WSL terminal.
- Activate this with `source .mlenv/bin/activate` command.
- Create a `requirements.txt` file and pip install libraries by running `pip install -r requirements.txt`.
- Notebooks are ready to execute. 
