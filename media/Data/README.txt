The data represents flood mapping results based on Sentinel-1 and the TU Wien flood mapping method (Bauer-Marschallinger et al., 2022) optimized for Austria. The results were produced in the context of the S1Floods.AT project and will be published as Roth et al., 2024 (to be submitted).

The dataset includes 4 events as seperate GeoJSON files including flooded areas represented as polygons. Each polygon has a time information and a layer assigned. There are 3 different layers:
- VV_flood: Open water, indicated by decreased backscatter in the VV polarization
- VV_increased: Potential flooded vegetation, indicated by increased backscatter in the VV polarization
- VH_flood: Open water or flooded vegetation, indicated by decreased backscatter in the VH polarization
