import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him 
into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""


# Create a function to return the most similar movie
def movie_search(sample):

        # Read in the movies.txt file and store the movie descriptions
        with open("movies.txt") as f:
                movie_descriptions = [line.strip() for line in f.readlines()]

        # Parse the input description
        input_doc = nlp(sample)

        # Compare the input description to each movie description and store the similarity scores
        similarities = [input_doc.similarity(nlp(movie_description)) for movie_description in movie_descriptions]

        # Return the movie with the highest similarity score
        output = movie_descriptions[similarities.index(max(similarities))]
        return print(output)

movie_search(description)