from django.http import JsonResponse
from django.shortcuts import render
import os
import json

def index(request):
    directory_path = os.path.join('media', 'Data')
    try:
        events = [f.split('.')[0] for f in os.listdir(directory_path) if f.endswith('.geojson')]
    except FileNotFoundError:
        events = []
    return render(request, 'visualization/show_map.html', {'events': events})

def load_geojson(request):
    event = request.GET.get('event')
    date = request.GET.get('date')
    layers = request.GET.get('layer').split(',')
    path = os.path.join('media', 'Data', f'{event}.geojson')
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            filtered_features = [
                feature for feature in data['features'] 
                if feature['properties']['datetime_1'].startswith(date[:8]) and feature['properties']['layer'] in layers
            ]
            data['features'] = filtered_features
            return JsonResponse(data, safe=False)
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)

def get_dates_for_event(request):
    event = request.GET.get('event')
    path = os.path.join('media', 'Data', f'{event}.geojson')
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            dates = sorted(set(feature['properties']['datetime_1'][:8] for feature in data['features']))
            return JsonResponse({'dates': dates})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def get_all_data(request):
    event = request.GET.get('event')
    path = os.path.join('media', 'Data', f'{event}.geojson')
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            # Organize data by date
            data_by_date = {}
            for feature in data['features']:
                date_key = feature['properties']['datetime_1'][:8]  # Assumes dates are stored in 'datetime_1'
                if date_key not in data_by_date:
                    data_by_date[date_key] = []
                data_by_date[date_key].append(feature)

            return JsonResponse(data_by_date, safe=False)
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)