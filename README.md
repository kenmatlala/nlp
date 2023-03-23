# SpaCy NLP Similarity Checker

This is a simple Python script that uses the SpaCy library to compare the similarity of words and sentences.
Requirements

## To run this script, you will need:

    - Python 3
    - SpaCy library

## Installation

    - Clone this repository to your local machine.
    - Install the required packages by running pip install -r requirements.txt.

## Usage

    1. Open a terminal window and navigate to the directory where the script is located.
    2. Run the script using the command python nlp_similarity_checker.py.
    3. The script will output the similarity scores for the provided words and sentences.

## Example

The following is an example of the output from running the script:

- 0.6616203070246372
- 0.2760836915896771
- 0.27946454109992976

- cat cat 1.0
- cat apple 0.3657356483937988
- cat monkey 0.6616202597618103
- cat banana 0.27946454215049744
- apple cat 0.3657356483937988
- apple apple 1.0
- apple monkey 0.3208929009437561
- apple banana 0.2760836845129145
- monkey cat 0.6616202597618103
- monkey apple 0.3208929009437561
- monkey monkey 1.0
- monkey banana 0.23193021106624603
- banana cat 0.27946454215049744
- banana apple 0.2760836845129145
- banana monkey 0.23193021106624603
- banana banana 1.0

- where did my dog go -  0.776470271741614
- Hello, there is my car -  0.7472687722603819
- I've lost my car in my car -  0.737390023497656
- I'd like my boat back -  0.6281737345324665
- I will name my dog Diana -  0.7472439287443694

## Notes

    This script uses the en_core_web_md model for English language processing. If you want to use a different model, you can change the nlp = spacy.load('en_core_web_md') line in the code.
    This script is provided as an example and may not be suitable for all use cases. Please ensure that you understand and comply with any relevant legal, ethical, and security requirements when using this script.

