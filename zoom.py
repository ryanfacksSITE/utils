from osgeo import gdal

def get_tiff_pixel_size_gdal(file_path: str) -> dict:
    """Get the pixel size of a TIFF file using GDAL"""
    try:
        dataset = gdal.Open(file_path)
        if not dataset:
            return {"error": "Could not open TIFF file."}
        geotransform = dataset.GetGeoTransform()
        if not geotransform:
            return {"error": "GeoTransform metadata not available."}
        pixel_width: float = geotransform[1]
        pixel_height: float = abs(geotransform[5])
        return {"pixel_width": pixel_width, "pixel_height": pixel_height}
    except Exception as e:
        return {"error": str(e)}


def optimal_zoom(resolution: float) -> str:
    """Determine the optimal zoom level based on resolution"""
    zoom: str = "16-23"
    try:
        if resolution <= 0.0108:
            zoom = "16-24"
        elif   0.0108 < resolution < 0.0250:
            zoom = "16-23"
        elif   0.0250 < resolution:
            zoom = "16-22"
    except Exception as e:
        print(f"Error: {e}")
        return zoom
    return zoom

#I made some changes
