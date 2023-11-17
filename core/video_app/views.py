from django.shortcuts import render, get_object_or_404
from django.http.response import StreamingHttpResponse

from .services import open_file
from .models import Video


def home_page(request):
    videos = Video.objects.all()
    return render(request, 'video_app/index.html', context={"videos": videos})


def video_detail(request, pk: int):
    _video = get_object_or_404(Video, pk=pk)
    return render(request, "video_app/detail.html", context={'video': _video})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)

    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

