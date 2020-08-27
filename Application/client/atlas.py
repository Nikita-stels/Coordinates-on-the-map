# import requests
# import folium
# from folium.plugins import MarkerCluster

# map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8)
# # Объединение маркеров в кластер
# marker_cluster = MarkerCluster().add_to(map)
# folium.Marker(location=[37.4074687,-122.086669], popup = "Text info", icon=folium.Icon(color = 'gray')).add_to(marker_cluster)
# folium.Marker(location=[37.4074687,-121.086669], popup = "Text info", icon=folium.Icon(color = 'gray')).add_to(marker_cluster)
# #-------------------------------
# folium.Marker(location=[37.4074687,-120.086669], popup = "Text info", icon=folium.Icon(color = 'gray')).add_to(map)

# # for coordinates in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
# #     folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)


# map.save("map1.html")