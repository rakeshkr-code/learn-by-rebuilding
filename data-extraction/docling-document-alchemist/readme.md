# Docling: The Document Alchemist

- **Repo_Name:** `learn-by-rebuilding`
- **Category:** `data-extraction`
- **Project:** `docling-document-alchemist`
- **Project Root Path:** `learn-by-rebuilding/data-extraction/docling-document-alchemist`

## Article Used
[Docling: The Document Alchemist](https://towardsdatascience.com/docling-the-document-alchemist/)

## Overview
This project re-implements and experiments with the concepts presented in the article **"Docling: The Document Alchemist"**.  

The goal is to explore how Docling converts unstructured documents (PDFs, DOCX, HTML) into structured formats that can be used in AI pipelines such as Retrieval-Augmented Generation (RAG).

---

## Objectives

- Understand the document conversion pipeline of Docling
- Convert PDF documents into structured formats
- Extract document components such as:
  - text
  - tables
  - images
  - layout information
- Export parsed documents into Markdown / JSON formats
- Explore how the output can be used for downstream AI tasks

---

## Project Structure

Here is the directory structure:
```
data-extraction/docling-document-alchemist/
├── readme.md
├── .gitignore
├── sample_docs/
│   ├── tesla_q10_sept_23_nonselectable.pdf
│   ├── tesla_q10_sept_23.html
│   ├── tesla_q10_sept_23.pdf
│   ├── tesla_q10_sept_23_page_11.png
│   ├── IFCT2017-table-1-1.pdf
│   └── IFCT2017-table-1-1-page-11.png
├── implementation.ipynb
├── experiments.ipynb
└── requirements.txt
```

---

## Dataset description

There is no download option for the given web link for [sample document](https://www.sec.gov/Archives/edgar/data/1318605/000162828023034847/tsla-20230930.htm) as a PDF. Base name of this document is `tesla_q10_sept_23`. So, I got 3 versions of it. (1) By using `[Ctrl] + [P]` to save as PDF, which is a scanned version, text is not selectable, (2) By saving the webpage HTML itself by `[Ctrl] + [S]`, (3) From the saved HTML I converted it into PDF using any online HTML to PDF converter, which makes the text selectable in the PDF. I took a screenshot of page no 11 of this document and made a image based document. 

Another set of document I personally have IFCT2017 Food Nutrition document (born digital text based PDF). Also I made a image based document from it by taking screenshot of page no 11 of this PDF. 

- `sample_docs/tesla_q10_sept_23_nonselectable.pdf`: This document suggested in the article, and this is the scanned version of PDF by `[Ctrl] + [P]` command against the webpage. 
- `sample_docs/tesla_q10_sept_23.html`: This is the direct html page. 
- `sample_docs/tesla_q10_sept_23.pdf`: This is the HTML to PDF converted version (with the help of online tools).
- `sample_docs/tesla_q10_sept_23_page_11.png`: Page number 11 screenshot image of this document. 
- `sample_docs/IFCT2017-table-1-1.pdf`: IFCT2017 Food Nutrition document PDF version (text based PDF). 
- `sample_docs/IFCT2017-table-1-1-page-11.png`: Food Nutrition document page no 11 screenshot image. 

--- 

## Description of Code files

- `implementation.ipynb`: In this notebook I tried to re-implement the exact process as much as possible shown in the article. I have documented the results I found. I also documented some of my reviews and comments. 
- [***] `experiments.ipynb`: In this notebook I did few more relavant experiments. 

## How to run?

- Create one venv using `python -m venv .mlenv` command in WSL terminal.
- Activate this with `source .mlenv/bin/activate` command.
- Create a `requirements.txt` file and pip install `docling`, and `pandas` by running `pip install -r requirements.txt`.
- Notebooks are ready to execute. 
