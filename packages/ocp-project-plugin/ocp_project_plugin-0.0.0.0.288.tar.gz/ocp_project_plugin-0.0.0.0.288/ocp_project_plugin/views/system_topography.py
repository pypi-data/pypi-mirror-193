from django.http import HttpResponse, HttpResponseNotFound


def sys_topography_file(request):
    file_location = '/repo/57e146958afea9fbeee5f634592c9590c55ebfa9.xml'

    try:
        with open(file_location, 'r') as f:
           file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="system_topography.xls"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response
