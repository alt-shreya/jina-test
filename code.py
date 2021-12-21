from jina import Document, DocumentArray, Executor, Flow

book1 = Document(tags={'attributes': {'title': 'The Catcher in the Rye', 'author': 'J D Sallinger'}})
book2 = Document(tags={'attributes': {'title': 'The Goldfinch', 'author': 'Donna Tartt'}})
book3 = Document(tags={'attributes': {'title': 'The Lobster', 'author': 'Yorgos Lanthimos'}})

books = DocumentArray(book1, book2, book3)
