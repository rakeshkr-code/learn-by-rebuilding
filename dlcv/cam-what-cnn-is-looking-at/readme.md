# CAM: What CNN is Looking at

- **Repo_Name:** `learn-by-rebuilding`
- **Category:** `dlcv`
- **Project:** `cam-what-cnn-is-looking-at`
- **Project Root Path:** `learn-by-rebuilding/dlcv/cam-what-cnn-is-looking-at`

## Article Used
[CAM - Class Activation Mapping](https://towardsdatascience.com/class-activation-mapping-using-transfer-learning-of-resnet50-e8ca7cfd657e/)


## Overview
This project re-implements and experiments with the concepts presented in the article mentioned above.  

The goal is to implement a powerful explainable AI (xAI) technique called CAM (Class Activation Map) that plots heatmap to visualize where/what exactly a CNN network is looking at. 

---

## Objectives

- Understand what is explainable AI (xAI)
- What are the techniques available that reveals what CNN exactly looking at for prediction of certain class
- Implementation of CAM (Class Activation Map)

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
