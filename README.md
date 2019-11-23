# TapSearch
 A simple program called TapSearch for TapChief &lt;> Coding Challenge for Tech Internship
# Description
 This is a simple program called TapSearch that achieves these objectives.

    1. It takes in multiple paragraphs of text, assigns a unique ID To each paragraph and stores the words to paragraph mappings on an  inverted index. This is similar to what elasticsearch does. This paragraph can also be referred to as a ‘document’

    2. Given a word to search for, it lists out the top 10 paragraphs in which the word is present

# Technologies Used
    1. Python
    2. Django
    3. Heroku
 
# Features
    1. clear - Clear the index and all indexed documents
    2. index - Index a given document (After having split the input into paragraphs a.k.a document )
    3. Search - Given a word, search for it and retrieve the top 10 paragraphs (Documents) that contain it
    4. Pdf - upload PDFs and index them. The uploaded PDFs are first parsed into text and then indexed as a document. Given a word to search, program will return the top 10 matches
    5. Image Search: classes implemented for image search
        a. Colordescriptor - a class for image descriptor to extract features from each image. When you put an image into an image descriptor, you will get features out the other end.
        b. Searcher -  a class that will define the actual similarity metric between two images.
    * NOTE - Only above code of above classes is implemented, integration with application remains

# Instructions
    1. Go to (Heroku) - https://enigmatic-garden-97449.herokuapp.com/
    2. Click on 'clear' to clear index
    3. Click on 'index' to index the document
    4. Click on 'Search' to search for word
    5. Click on 'Choose File' to insert pdf File
 
