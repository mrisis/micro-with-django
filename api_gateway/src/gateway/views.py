import json
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class ProxyView(APIView):

    def get_service_url(self, service):
        services = {
            'auth': 'http://auth:8000/api',
            'social': 'http://social:8000/api',
        }
        return services.get(service)

    def proxy_request(self, request, service, path):
        service_url = self.get_service_url(service)

        if not service_url:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)


        url = f"{service_url}/{service}/{path}"


        # تنظیم هدرها با حذف Host
        headers = {}
        for key, value in request.headers.items():
            if key.lower() != 'host':
                headers[key] = value

        try:
            method = request.method.lower()
            if method == 'get':
                response = requests.get(url, headers=headers, params=request.query_params)
            elif method == 'post':
                response = requests.post(url, headers=headers, json=request.data)
            elif method == 'put':
                response = requests.put(url, headers=headers, json=request.data)
            elif method == 'delete':
                response = requests.delete(url, headers=headers)
            else:
                return Response({'error': 'Method not supported'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            try:
                data = response.json()
            except ValueError:
                data = response.text

            return Response(data, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def get(self, request, path, service):
        return self.proxy_request(request, service, path)

    def post(self, request, path, service):
        return self.proxy_request(request, service, path)

    def put(self, request, path, service):
        return self.proxy_request(request, service, path)

    def delete(self, request, path, service):
        return self.proxy_request(request, service, path)