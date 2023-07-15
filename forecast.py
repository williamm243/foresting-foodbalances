# import streamlit as st
# import requests
# from PIL import Image
# import pandas as pd
# import pickle

# # Load the pickled forecast DataFrames for different areas
# with open('Kenya_forecast.pkl', 'rb') as f:
#     Kenya_forecast_df = pickle.load(f)

# with open('Uganda_forecast.pkl', 'rb') as f:
#     Uganda_forecast_df = pickle.load(f)

# with open('Tanzania_forecast.pkl', 'rb') as f:
#     Tanzania_forecast_df = pickle.load(f)

# with open('rwanda_forecast.pkl', 'rb') as f:
#     rwanda_forecast_df = pickle.load(f)

# # Set page config and layout
# st.set_page_config(page_title="Food Balance Forecast", page_icon="🌾", layout="wide")

# # Set page background color with CSS
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #ffffff;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Add page title and heading
# st.markdown("<h1 style='text-align: center; color: green;'>Food Balance Forecast</h1>", unsafe_allow_html=True)

# def main():
#     # Streamlit app code

#     # Add the flag of Kenya from the provided image URL
#     response = requests.get("https://github.com/Muramati/FAOStat-Dataset-Time-Series/raw/main/assets/Flag_of_Kenya.png")
#     #image = Image.open(BytesIO(response.content))
#     #st.image(image, caption="Flag of Kenya", use_column_width=True)

#     # Create a dropdown select for the area input
#     area_options = [None, 'Kenya', 'Uganda', 'Tanzania', 'Rwanda']
#     area_input = st.selectbox('Select the area:', area_options)

#     # Prompt the user to enter a specific year
#     target_year_input = st.text_input("Enter the target year for prediction:")

#     # Display the forecast for the target year based on the selected area
#     if st.button('Predict'):
#         forecast_df = None
#         if area_input == 'Kenya':
#             forecast_df = Kenya_forecast_df
#         elif area_input == 'Uganda':
#             forecast_df = Uganda_forecast_df
#         elif area_input == 'Tanzania':
#             forecast_df = Tanzania_forecast_df
#         elif area_input == 'Rwanda':
#             forecast_df = rwanda_forecast_df

#         if forecast_df is not None:
#             if target_year_input in forecast_df.index.year.astype(str).values:
#                 target_forecast = forecast_df.loc[forecast_df.index.year == int(target_year_input)]
#                 st.subheader(f"Forecast for {target_year_input}:")
#                 st.dataframe(target_forecast)
#             else:
#                 st.write(f"No forecast available for {target_year_input}.")
#         else:
#             st.write(f"No forecast available for the selected area.")

#     # Create a list of the predicted results and explanations
#     results_list = [
#         "**Domestic Supply Quantity:** The total amount of a particular agricultural commodity that is available for human consumption within a country. It is calculated as the sum of domestic production, imports, and changes in stocks, minus exports. It is measured in metric tons.",
#         "**Production:** The amount of a particular agricultural commodity that is produced within a country. It includes both crops and livestock products, and is measured in metric tons.",
#         "**Export Quantity:** The amount of a particular agricultural commodity that is exported from a country to other countries. It is measured in metric tons.",
#         "**Import Quantity:** The amount of a particular agricultural commodity that is imported into a country from other countries. It is measured in metric tons."
#     ]

#     # Display the predicted results and explanations as a list
#     with st.expander("Click here to see for more details"):
#         st.write(results_list)

# if __name__ == '__main__':
#     main()


import streamlit as st
import requests
from PIL import Image
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Disable the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the pickled forecast DataFrames for different areas
with open('Kenya_forecast.pkl', 'rb') as f:
    Kenya_forecast_df = pickle.load(f)

with open('Uganda_forecast.pkl', 'rb') as f:
    Uganda_forecast_df = pickle.load(f)

with open('Tanzania_forecast.pkl', 'rb') as f:
    Tanzania_forecast_df = pickle.load(f)

with open('rwanda_forecast.pkl', 'rb') as f:
    rwanda_forecast_df = pickle.load(f)

# Set page config and layout
st.set_page_config(page_title="Food Balance Forecast", page_icon="🌾", layout="wide")

# Set page background color with CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add page title and heading
st.markdown("<h1 style='text-align: center; color: green;'>Food Balance Forecast</h1>", unsafe_allow_html=True)

def main():
    # Streamlit app code

    # Add the flag of Kenya from the provided image URL
    response = requests.get("https://github.com/Muramati/FAOStat-Dataset-Time-Series/raw/main/assets/Flag_of_Kenya.png")
    #image = Image.open(BytesIO(response.content))
    #st.image(image, caption="Flag of Kenya", use_column_width=True)

    # Create a dropdown select for the area input
    area_options = [None, 'Kenya', 'Uganda', 'Tanzania', 'Rwanda']
    area_input = st.selectbox('Select the area:', area_options)

    # Prompt the user to enter the start year and end year
    start_year_input = st.text_input("Enter the start year:")
    end_year_input = st.text_input("Enter the end year:")

    # Display the line graphs and table for the selected area and specified start and end years
    if st.button('Show Line Graphs'):
        forecast_df = None
        if area_input == 'Kenya':
            forecast_df = Kenya_forecast_df
        elif area_input == 'Uganda':
            forecast_df = Uganda_forecast_df
        elif area_input == 'Tanzania':
            forecast_df = Tanzania_forecast_df
        elif area_input == 'Rwanda':
            forecast_df = rwanda_forecast_df

        if forecast_df is not None:
            if start_year_input.isdigit() and end_year_input.isdigit():
                start_year = int(start_year_input)
                end_year = int(end_year_input)
                if start_year <= end_year:
                    forecast_subset = forecast_df.loc[(forecast_df.index.year >= start_year) & (forecast_df.index.year <= end_year)]
                    if not forecast_subset.empty:
                        # Plot the line graphs
                        plt.figure(figsize=(10, 6))
                        plt.plot(forecast_subset.index, forecast_subset['Import quantity'], label='Import quantity')
                        plt.plot(forecast_subset.index, forecast_subset['Export quantity'], label='Export quantity')
                        plt.xlabel("Year")
                        plt.ylabel("Quantity")
                        plt.title(f"Import and Export Quantities from {start_year} to {end_year}")
                        plt.legend()
                        st.pyplot()

                        plt.figure(figsize=(10, 6))
                        plt.plot(forecast_subset.index, forecast_subset["Domestic Supply Quantity"], label='Domestic Supply Quantity')
                        plt.plot(forecast_subset.index, forecast_subset['Production'], label='Production')
                        plt.xlabel("Year")
                        plt.ylabel("Quantity")
                        plt.title(f"Domestic Supply Quantity and Production from {start_year} to {end_year}")
                        plt.legend()
                        st.pyplot()

                        # Display the table with forecasted values
                        st.subheader(f"Forecasted values from {start_year} to {end_year}:")
                        st.dataframe(forecast_subset)
                    else:
                        st.write("No forecast available for the specified start year and end year.")
                else:
                    st.write("Invalid input: Start year must be less than or equal to end year.")
            else:
                st.write("Invalid input: Start year and end year must be integers.")
        else:
            st.write(f"No forecast available for the selected area.")

    # Create a list of the predicted results and explanations
    results_list = [
        "**Domestic Supply Quantity:** The total amount of a particular agricultural commodity that is available for human consumption within a country. It is calculated as the sum of domestic production, imports, and changes in stocks, minus exports. It is measured in metric tons.",
        "**Production:** The amount of a particular agricultural commodity that is produced within a country. It includes both crops and livestock products, and is measured in metric tons.",
        "**Export Quantity:** The amount of a particular agricultural commodity that is exported from a country to other countries. It is measured in metric tons.",
        "**Import Quantity:** The amount of a particular agricultural commodity that is imported into a country from other countries. It is measured in metric tons."
    ]

    # Display the predicted results and explanations as a list
    with st.expander("Click here to see for more details"):
        st.write(results_list)

if __name__ == '__main__':
    main()
