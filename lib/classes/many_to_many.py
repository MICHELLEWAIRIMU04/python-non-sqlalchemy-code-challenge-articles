class Article:
    def __init__(self, author, magazine, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
            self._author = author
            self._magazine = magazine
            author._articles.append(self)
            magazine._articles.append(self)
        else:
            raise ValueError("Title must be between 5-50 characters.")
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of Author.")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be an instance of Magazine.")
    
    # Ensure title cannot be modified after instantiation
    @property
    def _is_title_set(self):
        return hasattr(self, "_title")
    
    # Ensure author and magazine can be modified after instantiation
    def __setattr__(self, name, value):
        if name in ['author', 'magazine'] and not hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Cannot modify {name} once set.")



class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            self._articles = []
        else:
            raise ValueError("Name must be a non-empty string.")
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
    
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))



class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16 and isinstance(category, str) and len(category) > 0:
            self._name = name
            self._category = category
            self._articles = []
        else:
            raise ValueError("Name must be between 2-16 characters and category must be a non-empty string.")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be between 2-16 characters.")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            authors[article.author] = authors.get(article.author, 0) + 1
        return [author for author, count in authors.items() if count > 2] if authors else None

