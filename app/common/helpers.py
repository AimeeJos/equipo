"""This module helps to download the generated files"""

from django.conf import settings
from django.http import StreamingHttpResponse
import os


def generate_excel_file(file_path):

    # Open the temporary file as a stream
    with open(file_path, "rb") as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            yield data


def download_file(foldername, filename):
    # print("=== ", foldername, filename)
    file_path = os.path.join(settings.MEDIA_ROOT, foldername, filename)
    try:
        response = StreamingHttpResponse(
            generate_excel_file(file_path),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    except Exception as e:
        print("---------------exception", e)
    response["Content-Disposition"] = f"attachment; filename={filename}"
    return response
