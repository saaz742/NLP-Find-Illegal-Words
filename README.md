# NLP-Find-Illegal-Words

Dr Asgari - Spring 2023

Sharif university

 - Sara Azarnoush

 - Mohammadreza Daviran

 - Nona Ghazizadeh

## Contents

[Document (Page 5)](https://github.com/saaz742/NLP-Find-Illegal-Words/blob/main/NLP_Spring1401_HW2.pdf)

[Report](https://github.com/saaz742/NLP-Find-Illegal-Words/blob/main/Project/NLP_HW2_report.pdf)

[Dataset](https://github.com/saaz742/NLP-Find-Illegal-Words/tree/main/Project/datasets)
  - [abbreviation](https://github.com/saaz742/NLP-Find-Illegal-Words/blob/main/Project/datasets/abbreviation.json)

[Crawler](https://github.com/saaz742/NLP-Find-Illegal-Words/tree/main/Project/crawler)
  - [abbreviation crawler](https://github.com/saaz742/NLP-Find-Illegal-Words/blob/main/Project/crawler/abbreviation_crawler.py)

[Notebook](https://github.com/saaz742/NLP-Find-Illegal-Words/tree/main/Project/notebook)
- [Find Illegal Words](https://github.com/saaz742/NLP-Find-Illegal-Words/blob/main/Project/notebook/NLP_HW2.ipynb)

## Introduction

In this project, our goal is to implement a system that has the ability to recognize illegal Persian words that may have been changed in certain ways. It should be noted that there are bots whose task is to recognize illegal words, but some of these bots cannot recognize these types of words when there are unrelated characters between their letters. Therefore, in this system, we want to recognize illegal words that may contain non-Persian letters (including English letters), numbers special characters, etc.

We also support two other modes in this system. The first one is when the user enters only its abbreviation instead of entering the whole word, for example, instead of writing the word "Islamic Republic", he writes the word "Ja", which is an abbreviation of the Islamic Republic. The second is the case in which he uses words of equivalent context, for example, he uses the word "greeting" instead of the word "healthy".

## Notebook's table of contents

- Requirements
  - Download libraries
  - Download the Persian fasttext model
  - Import libraries
- Preprocess the data
  - Normalizer and Lemmatizer
  - Download abbreviations
  - Read abbreviation
  - Numbers
  - Read the Persian fasttext model
- Process the data
  - Find Persian words
  - Find similar words in context
  - Print illegal words
  - Find words ignoring spaces
  - Print illegal words considering the spaces
- Test
  - Test without space in each word
  - Test with space in each word
  - Test with abbreviation in text
  - Test with normalizer
  - Test with lemmatizer
  - Test with context
