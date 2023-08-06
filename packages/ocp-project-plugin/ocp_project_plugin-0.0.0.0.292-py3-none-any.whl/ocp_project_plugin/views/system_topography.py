from django.http import HttpResponse, HttpResponseNotFound


def sys_topography_file(request):
    try:
        q = request.GET.get('q', '')
        ns = request.GET.get('ns', '')

        print(q)
        file_location = '/repo/' + q
        with open(file_location, 'r') as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type='application/xml')
        response['Content-Disposition'] = f'attachment; filename="{ns}.xml"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response
