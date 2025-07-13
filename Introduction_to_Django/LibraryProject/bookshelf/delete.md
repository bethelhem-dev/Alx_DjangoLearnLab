# DELETE Operation

## Command
```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()  # Expected output: <QuerySet []>
