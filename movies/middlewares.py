class MyMiddleware:

    def __init__(self, get_response):
        """
        This is one-time initialization, only called once, when server starts
        """
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):
        """
        This will call once per every request
        """
        print("This is called before view")
        response = self.get_response(request)
        print("This is called after view")
        return response
