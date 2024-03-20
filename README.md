# Web_Library

## Usage:

To launch:

```git clone```

```cd Web_Library```

```docker-compose up```

Postman to test HTTP methods:
```https://www.postman.com/```

Program runs on port 5000:
```localhost:5000```

### GET:

Read books:

```curl http://localhost:5000/books```

Read readers:

```curl http://localhost:5000/readers```

Read libraries:

```curl http://localhost:5000/libraries```

### POST:

Create book: 

```curl -X POST -H "Content-Type: application/json" -d '{"title": "New Book Title", "author": "New Book Author"}' http://localhost:5000/books```

Create reader:
```curl -X POST -H "Content-Type: application/json" -d '{"name": "New Name"}' http://localhost:5000/readers```

### PUT: ``` ```

Update book:

```curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Book Title", "author": "Updated Book Author"}' http://localhost:5000/books/1```
