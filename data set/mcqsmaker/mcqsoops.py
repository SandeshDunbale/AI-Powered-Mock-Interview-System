import spacy
import random

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

# Sample technical paragraph
technical_paragraph = """
Deep learning is a subset of machine learning that deals with neural networks: algorithms inspired by the structure and function of the brain's neurons. Machine learning algorithms use computational methods to "learn" information directly from data without relying on a predetermined equation as a model. Deep learning algorithms learn from large amounts of labeled data and automatically extract features from the data. These algorithms are used for tasks such as image and speech recognition, natural language processing, and more.
"""

# Process the text
doc = nlp(technical_paragraph)

# Extract nouns, verbs, and entities
nouns = [token.text for token in doc if token.pos_ == "NOUN"]
verbs = [token.text for token in doc if token.pos_ == "VERB"]
entities = [ent.text for ent in doc.ents]

# Function to generate technical MCQs
def generate_technical_mcq():
    # Placeholder for options
    options = ["A", "B", "C", "D"]

    # Randomly select a noun, verb, or entity
    chosen_word = random.choice(nouns + verbs + entities)

    # Extract sentences containing the chosen word
    relevant_sentences = [sent.text for sent in doc.sents if chosen_word in sent.text]

    if not relevant_sentences:
        return None, None  # Skip if no relevant sentences found

    # Randomly select one of the relevant sentences
    chosen_sentence = random.choice(relevant_sentences)

    # Shuffle options
    distractors = [chosen_word] + random.sample(nouns + verbs + entities, 3)
    random.shuffle(distractors)

    # Determine the correct answer
    correct_answer_index = distractors.index(chosen_word)
    correct_answer = options[correct_answer_index]

    # Create the MCQ format
    mcq = f"What does '{chosen_word}' refer to in the following context?\n\n"
    mcq += f"{chosen_sentence}\n"
    for i, option in enumerate(distractors):
        mcq += f"{options[i]}. {option}\n"

    return mcq, correct_answer

# Generate technical MCQs
num_questions = 5
print("Technical Multiple Choice Questions:")
for i in range(num_questions):
    mcq, correct_answer = generate_technical_mcq()
    if mcq:
        print(f"Question {i+1}:")
        print(mcq)
        print("Correct Answer:", correct_answer)
        print()
