class PageInfo:
    def __init__(self, skip: int, limit: int, totalCount: int, hasPreviousPage: bool, hasNextPage: bool):
        self.skip = skip
        self.limit = limit
        self.totalCount = totalCount
        self.hasPreviousPage = hasPreviousPage
        self.hasNextPage = hasNextPage

class PagePayload: 
    def __init__(self, page: PagePayload = PagePayload()):
        self.limit = limit
        self.skip = skip