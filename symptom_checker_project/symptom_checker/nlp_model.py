
# # Define a dictionary to categorize symptoms with automated responses
# symptom_responses = {
#     "respiratory": {
#         "fever": (
#             "Fever may indicate infection or inflammation. Stay hydrated, rest, and monitor your temperature. "
#             "If the fever is high or lasts more than 48 hours, consult a healthcare provider."
#         ),
#         "cough": (
#             "A persistent cough can be a sign of a respiratory infection, allergy, or irritation. "
#             "Monitor other symptoms and seek medical advice if it continues for more than a week."
#         ),
#         "shortness of breath": (
#             "Shortness of breath may result from respiratory, cardiac, or anxiety issues. "
#             "Seek immediate medical attention if breathing becomes difficult."
#         ),
#         "sneezing": (
#             "Sneezing is often a reaction to allergens or irritants. Try to identify potential allergens "
#             "and avoid exposure. If symptoms persist, consider allergy testing."
#         ),
#         "wheezing": (
#             "Wheezing could be a sign of asthma, respiratory infection, or airway irritation. "
#             "See a doctor if wheezing occurs frequently or alongside shortness of breath."
#         ),
#     },
#     "gastrointestinal": {
#         "nausea": (
#             "Nausea can result from infections, food sensitivities, or digestive issues. "
#             "Stay hydrated, avoid heavy foods, and rest. If nausea persists, see a healthcare provider."
#         ),
#         "vomiting": (
#             "Vomiting may indicate a gastrointestinal issue or infection. Stay hydrated with small sips of water. "
#             "Seek medical advice if vomiting continues or if dehydration occurs."
#         ),
#         "diarrhea": (
#             "Diarrhea can be due to infections, food poisoning, or dietary issues. Stay hydrated, "
#             "and avoid fatty foods. Consult a doctor if it lasts more than two days."
#         ),
#         "constipation": (
#             "Constipation can result from a low-fiber diet, dehydration, or lack of exercise. "
#             "Increase fiber intake, drink water, and consider mild physical activity. "
#             "Consult a doctor if it persists."
#         ),
#         "abdominal pain": (
#             "Abdominal pain may result from digestive issues, infection, or muscle strain. "
#             "Rest and avoid heavy meals. Seek medical advice if pain is intense or persistent."
#         ),
#     },
#     "musculoskeletal": {
#         "joint pain": (
#             "Joint pain may be caused by arthritis, injury, or overuse. Rest the joint, apply ice, and avoid strenuous activity. "
#             "If pain continues, consult a doctor."
#         ),
#         "muscle pain": (
#             "Muscle pain is often due to strain or injury. Rest, hydrate, and consider light stretching if it’s mild. "
#             "If pain persists, seek medical evaluation."
#         ),
#         "back pain": (
#             "Back pain may arise from poor posture, strain, or underlying issues. Practice good posture, avoid lifting heavy objects, "
#             "and see a doctor if it doesn’t improve."
#         ),
#         "neck pain": (
#             "Neck pain can result from strain, poor posture, or injury. Rest and avoid sudden movements. "
#             "Consult a doctor if it persists or is severe."
#         ),
#         "sprain": (
#             "A sprain may require rest, ice, compression, and elevation (RICE). Avoid putting weight on the injured area, "
#             "and consult a doctor if swelling or pain persists."
#         ),
#     },
#     "neurological": {
#         "headache": (
#             "Headaches can stem from stress, dehydration, or other factors. Drink water, rest, and reduce screen time. "
#             "Seek medical advice if headaches are frequent or severe."
#         ),
#         "dizziness": (
#             "Dizziness may be due to dehydration, low blood pressure, or an inner ear issue. Sit or lie down, drink water, "
#             "and if dizziness persists, consult a doctor."
#         ),
#         "tingling": (
#             "Tingling may be caused by nerve irritation, circulation issues, or pressure on nerves. "
#             "If tingling persists or affects a large area, seek medical advice."
#         ),
#         "numbness": (
#             "Numbness can result from nerve compression, injury, or circulation issues. "
#             "If numbness is persistent or extensive, consult a healthcare provider."
#         ),
#         "blurred vision": (
#             "Blurred vision can occur from eye strain, fatigue, or other conditions. Rest your eyes and ensure good lighting. "
#             "Seek medical advice if it persists or if you experience additional symptoms."
#         ),
#     },
#     # Add more categories here, such as Cardiovascular, Dermatological, Immunological, etc.
# }

# def diagnose_symptoms(symptom):
#     # Normalize the symptom input
#     symptom = symptom.lower()
#     # Search through categories and symptoms
#     for category, symptoms in symptom_responses.items():
#         if symptom in symptoms:
#             return symptoms[symptom]
#     return "Symptom not recognized. Please provide more details or consult a healthcare provider."

# import requests

# def diagnose_symptoms(symptom):
#     symptom = symptom.lower()
#     api_url = "https://api.aimlapi.com"  # Replace with the actual endpoint
#     headers = {
#         "Authorization": "3880a4477dce4e13ad522ea2d26b8efe",
#         "Content-Type": "application/json"
#     }
#     params = {
#         "symptom": symptom  # Use the actual symptom input here
#     }

#     response = requests.get(api_url, headers=headers, params=params)  # Changed to GET
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return "Error:", response.status_code, response.text

import requests
import openai

# Function to get medical information from OpenAI
def get_medical_response(query):
    response = openai.Completion.create(
      model="asst_OV10uc3NaRDq5SwalHQb5swv",  # Replace with a relevant model
      prompt=f"{query}",
      max_tokens=150,
      temperature=0.7
    )
    return response.choices[0].text.strip()

def get_health_info(symptoms):
    # URL of the community AI model API
    api_url = "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"  # Replace with actual API URL
    params = {'symptoms': symptoms}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        health_info = response.json()  # Assuming the response is in JSON format
        return health_info.get('advice', 'No specific advice available.')
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching health information: {e}"

def diagnose_symptoms(symptoms):
    # Normalize input to lower case
    symptoms = symptoms.lower()
    
    # Basic health-related keywords for validation
    health_keywords = ['fever', 'headache', 'cough', 'sore throat', 'muscle pain', 'joint pain', 'sprain', 'fracture', 'back pain', 'nausea']
    
    # Check if the symptoms contain any health-related keywords
    if not any(keyword in symptoms for keyword in health_keywords):
        return "It seems like your input isn't related to health. Please share valid health symptoms."
    
    # Call the health info API
    health_advice = get_health_info(symptoms)
    
    # Example of basic symptom diagnosis with more context
    if 'fever' in symptoms:
        return ("A fever often indicates an infection, such as a cold or flu. "
                "Stay hydrated, rest, and consider over-the-counter medications like acetaminophen or cold srupy but ensure you speak with your doctor. "
                "If the fever persists for more than a couple of days or is very high, consult a doctor. " + health_advice)
                
    elif 'headache' in symptoms:
        return ("Headaches can be caused by tension, dehydration, or even sinus issues. "
                "Try drinking more water, resting in a dark room, or using a cold compress. "
                "If headaches are severe or frequent, consider consulting a healthcare professional. " + health_advice)
                
    elif 'cough' in symptoms:
        return ("A cough might result from a respiratory infection, allergies, or even environmental irritants. "
                "Stay hydrated, use throat lozenges, and consider a humidifier. "
                "If it persists for more than a week or is accompanied by difficulty breathing, see a doctor. " + health_advice)
                
    elif 'sore throat' in symptoms:
        return ("A sore throat could be due to an infection or allergies. "
                "Gargling with salt water, staying hydrated, and using throat lozenges can help. "
                "If the soreness lasts longer than a few days or is severe, seek medical advice. " + health_advice)
                
    elif 'muscle pain' in symptoms:
        return ("Muscle pain can arise from strain, overexertion, or even stress. "
                "Rest, gentle stretching, and applying heat or ice can provide relief. "
                "If the pain persists or worsens, consider consulting a healthcare professional. " + health_advice)
                
    elif 'joint pain' in symptoms:
        return ("Joint pain might be a sign of arthritis or an injury. "
                "Resting the joint, applying ice, and taking anti-inflammatory medications can help. "
                "If the pain continues or is accompanied by swelling, consult a doctor. " + health_advice)
                
    elif 'sprain' in symptoms:
        return ("A sprain usually occurs from twisting or overstretching a ligament. "
                "Follow the RICE method: Rest, Ice, Compression, and Elevation. "
                "If the pain is severe or doesn’t improve, see a healthcare provider. " + health_advice)
                
    elif 'fracture' in symptoms:
        return ("If you suspect a fracture, it's important to seek medical attention immediately. "
                "In the meantime, immobilize the area and avoid putting weight on it. " + health_advice)
                
    elif 'back pain' in symptoms:
        return ("Back pain can result from muscle strain, poor posture, or herniated discs. "
                "Gentle stretching, applying heat, and maintaining good posture can help alleviate pain. "
                "If it persists or worsens, consider consulting a healthcare professional. " + health_advice)
                
    elif 'nausea' in symptoms:
        return ("Nausea can be caused by infections, dietary issues, or even anxiety. "
                "Try ginger tea, staying hydrated, and eating bland foods. "
                "If nausea continues or is severe, consult a doctor. " + health_advice)
                
    else:
        # If symptom is not recognized, query OpenAI
        medical_response = get_medical_response(f"What could be the possible reasons for the symptom: {symptoms}?")
        return f"Symptoms not recognized. Here's some information from an AI model: {medical_response}"

# Example usage
if __name__ == "__main__":
    user_symptoms = input("Please describe your symptoms: ")
    print(diagnose_symptoms(user_symptoms))