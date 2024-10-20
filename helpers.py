from geopy.geocoders import OpenCage
from geopy.distance import geodesic
import time 
from langchain_core.prompts import PromptTemplate
from MODEL import model
from prod_info import products
import uuid 

import os 
OPENCAGE_APIKEY= os.getenv("OPENCAGE_APIKEY")

geolocator = OpenCage(OPENCAGE_APIKEY)

def sleep_me():
    # st.write("sleep_me was called")
    time.sleep(2)

def get_coordinates_from_pincode(pincode):
    # sleep_me()
    location = geolocator.geocode(pincode)
    return (location.latitude, location.longitude)

def find_nearest_metro_city(pincode):
    # Metro city coordinates (example latitudes and longitudes)
    # sleep_me()
    metro_cities = {
        "New Delhi": {"pincode": "110001", "coordinates": (28.6139, 77.2090)},
        "Mumbai": {"pincode": "400001", "coordinates": (18.9388, 72.8354)},
        "Kolkata": {"pincode": "700001", "coordinates": (22.5726, 88.3639)},
        "Chennai": {"pincode": "600001", "coordinates": (13.0827, 80.2707)},
        "Bengaluru": {"pincode": "560001", "coordinates": (12.9716, 77.5946)},
        "Hyderabad": {"pincode": "500001", "coordinates": (17.3850, 78.4867)},
        "Ahmedabad": {"pincode": "380001", "coordinates": (23.0225, 72.5714)},
        "Pune": {"pincode": "411001", "coordinates": (18.5204, 73.8567)}
    }

    # Get coordinates of the input pin code
    input_coords = get_coordinates_from_pincode(pincode)
    if not input_coords:
        return "Invalid pin code or location not found."

    # Calculate distance to each metro city and find the nearest one
    nearest_city = None
    shortest_distance = float('inf')
    
    for city, data in metro_cities.items():
        city_coords = data["coordinates"]
        distance = geodesic(input_coords, city_coords).kilometers
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_city = city

    # Get pin code of the nearest metro city
    nearest_city_pincode = metro_cities[nearest_city]["pincode"]
    return nearest_city_pincode, nearest_city


def generate_product_description(prod_id):

    sleep_me()
    des = products[str(prod_id)]["technical_description"]

    template = """I have a technical description of a furniture product, and I need to transform it into a creative, 
            engaging, and customer-friendly product description that highlights the key features and benefits. 
            The goal is to make it appealing to potential buyers, focusing on how it will enhance their home 
            and lifestyle. 

            Please write a product description that:

            Explains the product’s features in a simple, easy-to-understand way.
            Highlights the product's design, functionality, and how it fits into a modern home.
            Appeals to customers' emotions, focusing on comfort, convenience, and aesthetic value.
            Encourages the customer to buy by explaining the value of the product.
            Make the description concise, but compelling.
            It should be about 300 words long
            Do not generate extra text
            
            Here's the technical description:

            {tech_des}"""
    
    prompt = PromptTemplate.from_template(template)

    chain = prompt | model 

    call_dict = {'tech_des': des}

    response = chain.invoke(call_dict).content
    return response

def get_unique_id():
    new_unique_id = str(uuid.uuid1())
    return new_unique_id

# import streamlit as st


# def raise_all_products_flag():
#     print("all raise function was called")
#     # st.write('raise all products flag function was called')
#     st.session_state['show_all_products_flag'] = True


# def raise_one_product_flag(prod_id:str):
#     sleep_me()
#     print("one raise function was called")
#     st.write('raise one product flag function was called')
#     st.session_state['show_one_product_flag'] = prod_id