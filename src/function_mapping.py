from visualisations.matthieu.visualisation import air_quality_over_time # might wanna update the name of this function to be more specific to the visualisation it creates
from visualisations.riccardo.visualisation_riccardo import daylight_hours
from visualisations.riccardo.visualisation2_riccardo import moon_illumination
from visualisations.guinness.guinness_vis import air_quality_by_country_over_time
from visualisations.joseph.joseph_vis import avg_temp_by_country_over_time
from visualisations.Chukwunonso.visualisation_Chukwunonso import temperature_celsius_to_feels_like_celsius
from visualisations.Chukwunonso.visualisation_Chukwunonso2 import Wind_mph_to_gust_mph

function_map = {
    'matthieu_1': air_quality_over_time,
    'riccardo_1': daylight_hours,
    "riccardo_2": moon_illumination,
    'guinness_1': air_quality_by_country_over_time,
    'joseph_1': avg_temp_by_country_over_time,
    'chukwunonso_1': temperature_celsius_to_feels_like_celsius,
    'chukwunonso_2': Wind_mph_to_gust_mph
}