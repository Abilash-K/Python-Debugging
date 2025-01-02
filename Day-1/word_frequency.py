def word_frequency(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

print(word_frequency('sample.txt'))




#Bugs
#The program doesn’t handle punctuation properly 
#(e.g., “hello.” and “hello” will be treated as different words).
#It assumes the file exists, but doesn't handle FileNotFoundError.