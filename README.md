# Video Generation and Content Processing

This project allows you to perform various video processing tasks, including generating videos from text prompts, generating hashtags from content, and processing videos to remove characters. It uses `moviepy` for video generation and `nltk` for natural language processing tasks.

## Features

1. **Remove Characters from Video**  
   This functionality allows you to remove specific characters from a video. This feature is a placeholder and you can add your own custom video processing logic here.

2. **Generate a Video from Text**  
   This functionality lets you generate a video based on a text prompt. The program will create images with text based on the input, and these images will be compiled into a video.

3. **Generate Content**  
   A simple content generation feature where the program generates content based on the provided prompt.

4. **Generate Hashtags**  
   Given a content string, the program will generate hashtags by analyzing the most frequent words (excluding stopwords and punctuation).

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `nltk`
  - `moviepy`
  
  You can install these dependencies by running the following command after creating a virtual environment.

## Installation

### Step 1: Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone <https://github.com/sourabh2104/GenAI_Models.git>



### Create a Virtual Enviornment

```bash
python3-m venv venv

source venv/bin/activate



### Install dependencies:

```bash
pip install -r requirements.txt


pip install nltk moviepy

```bash

```bash
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```bash


```bash

python main.py

```bash