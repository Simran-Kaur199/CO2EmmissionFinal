import pandas as pd
import streamlit as st
# from sklearn.linear_model import LogisticRegression
# from pickle import load
import pickle

# import the model
# pipe = pickle.load(open('linear_pipe.pkl', 'rb'))
pipe = pickle.load(open('svm_pipe.pkl', 'rb'))
# data = pickle.load(open('data.pkl', 'rb'))

st.title('CO2 Emission')

st.sidebar.header('User Input Parameters')


def user_input_features():
    make = st.selectbox('Make', ['FORD', 'CHEVROLET', 'BMW', 'MERCEDES-BENZ', 'PORSCHE', 'GMC', 'TOYOTA',
                                 'AUDI', 'NISSAN', 'MINI', 'JEEP', 'KIA', 'VOLKSWAGEN', 'HYUNDAI', 'DODGE',
                                 'HONDA', 'CADILLAC', 'LEXUS', 'MAZDA', 'SUBARU', 'JAGUAR', 'VOLVO', 'BUICK',
                                 'INFINITI', 'LINCOLN', 'LAND ROVER', 'MITSUBISHI', 'RAM', 'CHRYSLER', 'FIAT',
                                 'MASERATI', 'ACURA', 'ROLLS-ROYCE', 'ASTON MARTIN', 'LAMBORGHINI', 'BENTLEY',
                                 'SCION', 'ALFA ROMEO', 'GENESIS', 'SMART', 'SRT', 'BUGATTI'])
    engine_size = st.sidebar.slider('Engine Size', 0.9, 6.25)
    cylinders = st.selectbox('Cylinders', [3, 4, 5, 6, 8, 9, 10, 12, 16])
    transmission = st.selectbox('Transmission', ['AS', 'A', 'M', 'AM', 'AV'])
    fuel_type = st.selectbox('Fuel Type', ['X', 'Z', 'E', 'D'])
    fuel_con_hw = st.sidebar.slider('Fuel Consumption in Highway', 4.0, 20.6)
    fuel_con_comb = st.sidebar.slider('Fuel Consumption Combination in mpg', 11.0, 69.0)
    vehicle_types = ['SUV', 'Truck or Van', 'Sedan', 'Compact']

    # Create a radio button for selecting a vehicle type
    selected_vehicle_type = st.radio('Select a vehicle type:', vehicle_types)

    # Convert the selected option to binary values
    vehicle_type_dict = {vehicle: 1 if vehicle == selected_vehicle_type else 0 for vehicle in vehicle_types}

    # Use the binary values in your further analysis or processing
    SUV = vehicle_type_dict['SUV']
    Truck_Van = vehicle_type_dict['Truck or Van']
    Sedan = vehicle_type_dict['Sedan']
    Compact = vehicle_type_dict['Compact']

    data1 = {'make': make,
             'engine_size': engine_size,
             'cylinders': cylinders,
             'transmission': transmission,
             'fuel_type': fuel_type,
             'fuel_consumption_hwy': fuel_con_hw,
             'fuel_consumption_comb(mpg)': fuel_con_comb,
             'SUV': SUV,
             'Truck-Van': Truck_Van,
             'Sedan': Sedan,
             'Compact': Compact}
    features = pd.DataFrame(data1, index=[0])
    return features


df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

if st.button('Predict'):
    prediction = pipe.predict(df)

    st.subheader('Predicted Result')
    st.write(prediction)
