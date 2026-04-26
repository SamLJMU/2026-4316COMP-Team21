from visualisations.matthieu.visualisation import air_pollution_relations # might wanna update the name of this function to be more specific to the visualisation it creates
from visualisations.riccardo.visualisation_riccardo import daylight_hours
from visualisations.riccardo.visualisation2_riccardo import moon_illumination
from visualisations.guinness.guinness_vis import air_quality_by_country_over_time
from visualisations.joseph.joseph_vis import avg_temp_by_country_over_time
from visualisations.Chukwunonso.visualisation_Chukwunonso import temperature_celsius_to_feels_like_celsius
from visualisations.Chukwunonso.visualisation_Chukwunonso2 import Wind_mph_to_gust_mph
from visualisations.Daniels.daniels_vis import userdata_wind_speed
from visualisations.Daniels.daniels_vis2 import userdata_uv_index
from visualisations.toprak.toprak_vis import humidity_vs_cloud_over_time
from visualisations.toprak.toprak_vis2 import cloud_vs_feels_like_temp_over_time
from visualisations.sam.visualisation_sam1 import air_pressure_and_percipitation
from visualisations.sam.visualisation_sam2 import daylight_and_percipitation


function_map = {
    'matthieu_1': air_pollution_relations,
    'riccardo_1': daylight_hours,
    "riccardo_2": moon_illumination,
    'guinness_1': air_quality_by_country_over_time,
    'joseph_1': avg_temp_by_country_over_time,
    'chukwunonso_1': temperature_celsius_to_feels_like_celsius,
    'chukwunonso_2': Wind_mph_to_gust_mph,
    'daniels_1' : userdata_wind_speed,
    'daniels_2' : userdata_uv_index,
    'toprak_1' : humidity_vs_cloud_over_time,
    'toprak_2' : cloud_vs_feels_like_temp_over_time,
    'sam_1': air_pressure_and_percipitation,
    'sam_2': daylight_and_percipitation
}