from threading import Condition
import streamlit as st
import joblib
import pandas as pd

dataset_df = pd.read_csv('/content/CleanData.csv')

model = joblib.load('/content/ML_Model.pkl')


input_columns = [ 'Type','Location','Area', 'Rooms','Bathrooms','Condition','Air conditioning'
,'Garden','Heating','Furnished','Equipped kitchen','Double glazing','Security system','Terrace',
'Elevator', 'Satellite dish','Oven','Mountains views'
,'Internet','Garage','Pool','Concierge','Reinforced Door','Microwave','Fridge','TV','Washing machine','Sea views']


location_options = dataset_df['Location'].unique().tolist()
condition_options = dataset_df['Condition'].unique().tolist()
type_options = dataset_df['Type'].unique().tolist()
Air_conditioning_options = dataset_df['Air conditioning'].unique().tolist()
Garden_options = dataset_df['Garden'].unique().tolist()
Heating_options = dataset_df['Heating'].unique().tolist()
Furnished_options = dataset_df['Furnished'].unique().tolist()
Equipped_kitchen_options = dataset_df['Equipped kitchen'].unique().tolist()
Double_glazing_options = dataset_df['Double glazing'].unique().tolist()
Security_system_options = dataset_df['Security system'].unique().tolist()
Terrace_options = dataset_df['Terrace'].unique().tolist()
Elevator_options = dataset_df['Elevator'].unique().tolist()
Satellite_dish_options = dataset_df['Satellite dish'].unique().tolist()
Mountains_views_options = dataset_df['Mountains views'].unique().tolist()
Internet_options = dataset_df['Internet'].unique().tolist()
Oven_options = dataset_df['Oven'].unique().tolist()
Garage_options = dataset_df['Garage'].unique().tolist()
Pool_options = dataset_df['Pool'].unique().tolist()
Concierge_options = dataset_df['Concierge'].unique().tolist()
Reinforced_Door_options = dataset_df['Reinforced Door'].unique().tolist()
Microwave_options = dataset_df['Microwave'].unique().tolist()
Fridge_options = dataset_df['Fridge'].unique().tolist()
TV_options = dataset_df['TV'].unique().tolist()
Washing_machine_options = dataset_df['Washing machine'].unique().tolist()
Sea_views_options = dataset_df['Sea views'].unique().tolist()


columns = ['Sea views', 'Washing machine', 'TV', 'Mountains views', 'Reinforced Door',
                        'Air conditioning', 'Garden', 'Heating', 'Fridge', 'Microwave', 'Concierge',
                        'Pool', 'Garage', 'Internet', 'Oven', 'Elevator', 'Satellite dish',
                        'Terrace', 'Security system', 'Double glazing', 'Equipped kitchen', 'Furnished']


st.title('House Price Prediction')


inputs = {}
for col in input_columns:
    if col == 'Location':
        inputs[col] = st.selectbox(f'Select {col}', location_options)
    elif col == 'Condition':
      inputs[col] = st.selectbox(f'Select {col}', condition_options)
    elif col == 'Type':
      inputs[col] = st.selectbox(f'Select {col}', type_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Oven_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Air_conditioning_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Garden_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Heating_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Furnished_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Equipped_kitchen_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Double_glazing_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Security_system_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Terrace_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Elevator_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Satellite_dish_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Mountains_views_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Internet_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Garage_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Pool_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Concierge_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Reinforced_Door_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Microwave_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Fridge_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', TV_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Washing_machine_options)
    elif col in columns:
      inputs[col] = st.selectbox(f'Select {col}', Sea_views_options)
    else:
        inputs[col] = st.number_input(f'Enter {col}', value=0.0)

# Ajouter un bouton pour effectuer la prédiction
if st.button('Predict'):
    # Convertir les entrées en DataFrame
    input_data = pd.DataFrame([inputs])

    # Effectuer la prédiction avec le modèle chargé
    prediction = model.predict(input_data)

    # Afficher la prédiction
    st.write('Predicted Price:', prediction)
