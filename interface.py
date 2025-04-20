import gradio as gr
import pandas as pd
import joblib

# Step 1: Load the trained model
model = joblib.load("house_price_model.pkl")

# Step 2: Define logic to predict price
def predict_price(rooms, area, age):
    # Step 3: Use the received slider values to make a DataFrame
    new_house = pd.DataFrame({
        'rooms': [rooms],
        'area': [area],
        'age': [age],
    })

    # Step 4: Predict with the model
    predicted_price = model.predict(new_house)[0]
    
    # Step 5: Return formatted result
    return f"€ {predicted_price:,.2f}"

# Step 6: Gradio UI
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Slider(1, 5, step=1, label="Number of Rooms"),
        gr.Slider(30, 200, step=1, label="Area (m²)"),
        gr.Slider(0, 50, step=1, label="House Age (years)"),
    ],
    outputs=gr.Textbox(label="Predicted House Price"),
    title="🏠 House Price Predictor",
    description="Adjust the sliders to estimate the price of a house based on its features.",
    theme="default"
)

# Step 7: Run the app
interface.launch()
