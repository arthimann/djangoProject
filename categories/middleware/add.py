from django.http import HttpResponse


class AddCategoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_exception = 0

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if len(request.POST) > 0:
            if request.POST['title'] == 'wtf':
                raise Exception('aaaaaaa', 401)
        return None

    def process_exception(self, request, exception):
        self.num_exception += 1
        return HttpResponse('categories/test.html')
