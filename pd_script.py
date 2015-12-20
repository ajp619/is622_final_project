def mapper(_, text, writer):
    for word in text.split():
        writer.emit(word, "1")
