import geopandas as gpd
import numpy as np
from sklearn.cluster import DBSCAN
from shapely.geometry import Point

def perform_clustering_and_convert(geojson_path, eps=100, min_samples=5):
    # Load the data
    gdf = gpd.read_file(geojson_path)

    # Check if the data needs to be projected (assuming it's not already in EPSG:3395)
    if gdf.crs != 'epsg:3395':
        gdf = gdf.to_crs(epsg=3395)  # Project to World Mercator for accurate distance measurements

    # Extract coordinates for clustering
    coords = np.array(list(zip(gdf.geometry.x, gdf.geometry.y)))

    # Perform DBSCAN clustering
    db = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean')
    labels = db.fit_predict(coords)

    # Assign clusters back to the GeoDataFrame
    gdf['cluster'] = labels

    # Aggregate cluster data, calculating mean coordinates and other properties as necessary
    clustered = gdf.groupby('cluster').apply(
        lambda group: Point(group.geometry.x.mean(), group.geometry.y.mean())
    ).reset_index(name='geometry')

    # Create a new GeoDataFrame from the clustered data
    clustered_gdf = gpd.GeoDataFrame(clustered, geometry='geometry')
    clustered_gdf.crs = 'epsg:3395'

    # Convert to WGS 84 (lat/lon) for display purposes
    clustered_gdf = clustered_gdf.to_crs(epsg=4326)

    return clustered_gdf.to_json()
