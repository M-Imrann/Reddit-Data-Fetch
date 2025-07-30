class FilterPost:
    """
    Filter the posts based on the criteria that
    is above the minimum score.
    """
    def __init__(self, min_score):
        self.min_score = min_score

    def filter_post(self, posts):
        return list(filter(lambda post: post.score >= self.min_score, posts))


class PostIterator:
    """
    PostIterator is used to iterate on the posts.
    """
    def __init__(self, posts):
        self._posts = posts
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._posts):
            post = self._posts[self._index]
            self._index += 1
            return post
        raise StopIteration


class PostGenerator:
    """
    Create a generator function using `yield`
    to lazily iterate over the filtered posts.
    """
    def __init__(self, posts):
        self.posts = posts

    def post_generator(self):
        for post in self.posts:
            yield post


class PostZipper:
    """
    Use the `zip` function in combination with lambda
    functions to pair selected fields from each post.
    """
    def __init__(self, posts):
        self.posts = posts

    def zip_title_url(self):
        return list(zip(
            map(lambda p: p.title, self.posts),
            map(lambda p: p.url, self.posts)
        ))
