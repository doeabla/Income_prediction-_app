import streamlit as st
import pandas as pd
import joblib
from PIL import Image
from sklearn.tree import DecisionTreeClassifier

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# Header style
header_style = """
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 20px;
"""

# Header at the top of the page
st.markdown(
    f'<div style="{header_style}">'
    f'<h1>WELCOME TO ZANZIBAR GROUP</h1>'
    f'<h2>INCOME PREDICTION APP</h2>'
    f'<p>This is a simple app for predicting income level of people, thereby aiding policymakers in managing and preventing income inequality globally.</p>'
    f'</div>',
    unsafe_allow_html=True)


# Specify the path to your image file
image_path = "C:/Users/USER/Desktop/Capstone_Project/new_work/pics/income_prediction.jpeg"
image = Image.open(image_path)

# Set up the layout with three columns
col1, col2, col3 = st.columns([1, 2, 1])

# Display the image in the middle column with a specific width
image_width = 800  
col2.image(image, caption='Sales Image', width=image_width)

# Load the pipeline
file_path_pipeline = "dtree_pipeline.joblib"
loaded_pipeline = joblib.load(file_path_pipeline)

# Load the label encoder
file_path_encoder = "labelencoderbal.joblib"
loaded_encoder = joblib.load(file_path_encoder)

# Function to predict income limit
def predict_income_limit(args):
    try:
        input_data = pd.DataFrame([args])
        predicted_income_level = loaded_pipeline.predict(input_data)
        decoded_income_level = loaded_encoder.inverse_transform(predicted_income_level)
        return decoded_income_level[0]
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("Employee Income Prediction App")
    st.write("Enter Employee information to predict Income limit")

    # Input components
    age = st.number_input("Age", min_value=0, max_value=100, value=30)
    gender = st.radio("Gender", ["male", "female"])
    education = st.selectbox("Education", ["Bachelors Degree", "High School Graduate", "Some College (No Degree)", "Masters Degree", "Associates Degree (Academic Program)", "Professional School Degree", "11th Grade", "9th Grade", "Children", "7th and 8th Grade", "10th Grade", "12th Grade No Diploma", "5th or 6th Grade", "Less than 1st Grade"])
    work_class = st.selectbox("Work Class", ["Self-employed-not incorporated", "Private", "Federal government", "Local government", "Self-employed-incorporated", "State government", "Without pay", "Never worked"])
    marital_status = st.selectbox("Marital Status", ["Married-A F spouse present", "Never married", "Divorced", "Widowed", "Separated", "Married-spouse absent", "Married-civilian spouse present"])
    race = st.selectbox("Race", ["White", "Black", "Asian or Pacific Islander", "Other"])
    is_hispanic = st.selectbox("Is Hispanic", ["All other", "Mexican-American", "Mexican (Puerto Rico Only)", "Central or South American", "Cuban", "Do not know", "Chicano", "Puerto Rican"])
    employment_commitment = st.selectbox("Employment Commitment", ["Full-time schedules", "Not in labor force", "PT for non-econ reasons usually FT", "PT for econ reasons usually PT", "Unemployed full-time", "PT for econ reasons usually FT", "Unemployed part- time", "PT for non-econ reasons usually PT", "PT for econ reasons usually FT", "Unemployed part-time"])
    wage_per_hour = st.number_input("Wage Per Hour", min_value=0, value=10)
    working_week_per_year = st.number_input("Working Weeks Per Year", min_value=0, value=40)
    industry_code_main = st.selectbox("Industry Code Main", ["Other professional services", "Retail trade", "Construction", "Finance insurance and real estate", "Manufacturing-nondurable goods", "Transportation", "Public administration", "Manufacturing-durable goods", "Business and repair services", "Mining", "Social services", "Educational services", "Health services", "Personal services except private HH", "Communications"])
    occupation_code_main = st.selectbox("Occupation Code Main", ["Executive admin and managerial", "Sales", "Other service", "Craft repair and kindred", "Laborers except construction", "Operatives and kindred", "Professional specialty", "Adm support including clerical", "Private household services", "Transport equipment operatives", "Technicians and related support", "Farming forestry and fishing", "Precision production craft & repair", "Machine operators assmblrs & inspctrs", "Protective services", "Transportation and material moving"])
    tax_status = st.selectbox("Tax Status", ["Single", "Joint both under 65", "Joint both 65+", "Joint one under 65 & one 65+", "Joint one under 65 & one 65+"])
    citizenship = st.selectbox("Citizenship", ["native", "foreign born- U S citizen by naturalization", "foreign born- Not a citizen of U S"])

    # Prediction button
    if st.button("Predict"):
        employee_info = {
            "age": age, "gender": gender, "education": education,
            "work_class": work_class, "marital_status": marital_status,
            "race": race, "is_hispanic": is_hispanic,
            "employment_commitment": employment_commitment,
            "wage_per_hour": wage_per_hour,
            "working_week_per_year": working_week_per_year,
            "industry_code_main": industry_code_main,
            "occupation_code_main": occupation_code_main,
            "tax_status": tax_status, "citizenship": citizenship
        }

        prediction = predict_income_limit(employee_info)
        st.success(f"The predicted income limit is: {prediction}")

# Set up the layout with three columns
col1, col2, col3 = st.columns([1, 2, 1])
# Designer information
designer_info = "Designed by: Team Zanzibar"

# Team members' names
team_members = ["Doe Edinam & Enoch Taylor-Nketiah,Kofi Asare Bamfo"]

# Display the designer information and team members in the right-bottom corner
col3.markdown(
    f'<div style="position: absolute; bottom: 10px; right: 10px; font-weight: bold;">'
    f'{designer_info}<br/>'
    f'Team Members: {", ".join(team_members)}'
    f'</div>',
    unsafe_allow_html=True)

if __name__ == "__main__":
    main()
