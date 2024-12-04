#!/usr/bin/env python
# coding: utf-8

# Petit Dassilva<br>
# Troy University<br>
# Adv Artificial Intelligence<br>
# Homework 7<br>
# 
# This week, you will continue to work on the same textual data File  Download Fileas you did the last week. 
# 
# Remove all the punctuations and non-English words, then count the number of the rest of the words in the file
# Using the words after step 1 to build a word dictionary, all the words in the dictionary are unique (e.g. the word "But" and "but" should be considered as the same word)
# Count the number of distinct words in your dictionary
# The words in the dictionary should be displayed in an alphabetic order
# Select three sentences from the file, then use any POS tagging tools to identify POS tags in the selected sentences.
# The source code file and the output of your program are required to submit to Canvas. 

# In[5]:


import re
import string
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag


# In[6]:


# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to clean the text
def clean_text(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    
    # Extract English words
    words = re.findall(r'\b[a-z]+\b', text)
    
    return words

# Process the file to count words and generate the dictionary
def process_file(file_path): 
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Clean the text (remove punctuation and non-English words)
    words = clean_text(text)
    
    # Count the total number of words
    total_words = len(words)
    
    # Create a set of unique words (dictionary) and sort them alphabetically
    unique_words = sorted(set(words))
    
    return total_words, unique_words, words

# Perform POS tagging on selected sentences
def pos_tagging_on_sentences(text, num_sentences=3):
    sentences = sent_tokenize(text)
    
    # Select random sentences
    selected_sentences = sentences[:num_sentences]
    tagged_sentences = [pos_tag(word_tokenize(sentence)) for sentence in selected_sentences]
    
    return selected_sentences, tagged_sentences

# Path to the text file
file_path = r'C:\Users\dassi\Downloads\Shakespeare.txt'  # Update this path as needed

# Process the file
total_words, unique_words, all_words = process_file(file_path)

# Output results
print(f"Total number of words: {total_words}")
print(f"Total number of unique words: {len(unique_words)}")
print("\nUnique words (alphabetically ordered):")
print(unique_words[:20])  # Display first 20 unique words for brevity

# Perform POS tagging
with open(file_path, 'r') as file:
    text = file.read()

selected_sentences, tagged_sentences = pos_tagging_on_sentences(text)

print("\nPOS Tagging on Selected Sentences:")
for sentence, tagged in zip(selected_sentences, tagged_sentences):
    print(f"Sentence: {sentence}")
    print(f"Tagged: {tagged}\n")


# In[ ]:




