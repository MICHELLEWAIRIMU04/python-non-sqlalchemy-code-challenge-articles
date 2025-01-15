class Article:
     def __init__(self, author: 'Author', magazine: 'Magazine', title: str):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")

        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self._title = title

    @property
    def title(self) -> str:
        return self._title


class Author:
    def __init__(self, name: str):
         if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")

        self.name = name

    @property
     def articles(self) -> List['Article']:
        return self._articles

    def magazines(self) -> List['Magazine']:
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine: 'Magazine', title: str) -> 'Article':
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")

        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)
        return article

    def topic_areas(self) -> Optional[List[str]]:
        categories = {magazine.category for magazine in self.magazines()}
        return list(categories) if categories else None


class Magazine:
    def __init__(self, name:str, category:str):
     if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        self.name = name
        self.category = category
        self._articles: List[Article] = []
        Magazine._instances.append(self)
        

    @property
    def articles(self) -> List['Article']:
        return self._articles

    def add_article(self, article: 'Article') -> None:
        self._articles.append(article)

    def contributors(self) -> List['Author']:
        return list({article.author for article in self._articles})

    def article_titles(self) -> Optional[List[str]]:
        return [article.title for article in self._articles] or None

    def contributing_authors(self) -> Optional[List['Author']]:
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2] or None

    @classmethod
    def top_publisher(cls) -> Optional['Magazine']:
        if not cls._instances:
            return None
        return max(cls._instances, key=lambda magazine: len(magazine.articles))
 