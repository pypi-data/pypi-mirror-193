from django.http import HttpResponse, HttpResponseNotFound


def sys_topography_file(request):
    # prefix = 57e146958afea9fbeee5f634592c9590c55ebfa9.xml'

    try:
        q = request.GET.get('q', '')

        print(q)
        file_location = '/repo/' + q
        with open(file_location, 'r') as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="system_topography.xml"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response
