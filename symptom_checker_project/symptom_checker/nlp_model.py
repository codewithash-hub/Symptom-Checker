# def diagnose_symptoms(symptoms):
#     # Placeholder for NLP logic
#     if 'fever' in symptoms:
#         return 'You might have an infection. Please consult a doctor.'
#     elif 'headache' in symptoms:
#         return 'You might be experiencing stress or dehydration.'
#     else:
#         return 'Symptoms not recognized. Please provide more details.'


# def diagnose_symptoms(symptoms):
#     # Your NLP logic to process symptoms
#     # For example:
#     diagnosis = "Based on your symptoms, it could be a common cold."  # Example response
#     return diagnosis


# def diagnose_symptoms(symptoms):
#     # Normalize input to lower case
#     symptoms = symptoms.lower()
    
#     if 'fever' in symptoms:
#         return (
#             "You might have an infection, as fever often indicates that your body is fighting an infection. "
#             "It could be viral or bacterial. Keep yourself hydrated and consider taking rest. Please consult "
#             "a doctor for a thorough diagnosis and appropriate treatment if the fever persists or is high."
#         )
#     elif 'headache' in symptoms:
#         return (
#             "You might be experiencing stress, dehydration, or even a minor cold, which can cause headaches. "
#             "Other factors, like sleep deprivation or prolonged screen time, may also contribute. Try drinking "
#             "water, resting, and avoiding screens. If it continues or intensifies, consult a healthcare professional."
#         )
#     elif 'cough' in symptoms:
#         return (
#             "A cough could indicate a respiratory infection, allergies, or even acid reflux. Pay attention to "
#             "whether it is dry or productive, and monitor any other symptoms like a sore throat or fever. "
#             "If the cough persists or is severe, consider seeing a doctor to rule out conditions such as bronchitis."
#         )
#     elif 'sore throat' in symptoms:
#         return (
#             "A sore throat might suggest a throat infection, like strep throat, or could be due to allergies. "
#             "Gargling with warm salt water can help alleviate discomfort. Please consult a healthcare professional, "
#             "especially if accompanied by fever or difficulty swallowing."
#         )
#     elif 'muscle pain' in symptoms:
#         return (
#             "Muscle pain is often caused by muscle strain, overexertion, or minor injuries. Ensure you get adequate rest, "
#             "stay hydrated, and consider gentle stretching if the pain isn't severe. If it doesn't improve, consult a "
#             "doctor as it could indicate a more serious underlying condition."
#         )
#     elif 'joint pain' in symptoms:
#         return (
#             "Joint pain may be a sign of arthritis, injury, or inflammation. Try resting and avoiding strenuous activity. "
#             "Over-the-counter pain relief may help, but it's best to consult a doctor for a proper diagnosis, especially if "
#             "swelling or redness accompanies the pain."
#         )
#     elif 'sprain' in symptoms:
#         return (
#             "A sprain can benefit from the RICE method: Rest, Ice, Compression, and Elevation. It's essential to avoid putting "
#             "pressure on the injured area. If pain or swelling continues, consult a doctor to ensure there's no ligament damage."
#         )
#     elif 'fracture' in symptoms:
#         return (
#             "If you suspect a fracture, it's important to seek immediate medical attention. Avoid moving the affected area, "
#             "and try to immobilize it as much as possible until you receive professional care."
#         )
#     elif 'back pain' in symptoms:
#         return (
#             "Back pain can result from muscle strain, poor posture, or even herniated discs. Avoid heavy lifting and practice "
#             "good posture. If the pain persists, consult a doctor as they may recommend imaging tests or physical therapy."
#         )
#     elif 'nausea' in symptoms:
#         return (
#             "Nausea can have various causes, including infections, food intolerance, or digestive issues. Try to rest and "
#             "drink clear fluids. Avoid rich or spicy foods until you feel better. If nausea persists or is accompanied by "
#             "vomiting or fever, consult a healthcare provider."
#         )
#     else:
#         return (
#             "Symptoms not recognized. Please provide more details for a better assessment, or consider consulting a "
#             "healthcare provider for a comprehensive evaluation."
#         )


# Define a dictionary to categorize symptoms with automated responses
symptom_responses = {
    "respiratory": {
        "fever": (
            "Fever may indicate infection or inflammation. Stay hydrated, rest, and monitor your temperature. "
            "If the fever is high or lasts more than 48 hours, consult a healthcare provider."
        ),
        "cough": (
            "A persistent cough can be a sign of a respiratory infection, allergy, or irritation. "
            "Monitor other symptoms and seek medical advice if it continues for more than a week."
        ),
        "shortness of breath": (
            "Shortness of breath may result from respiratory, cardiac, or anxiety issues. "
            "Seek immediate medical attention if breathing becomes difficult."
        ),
        "sneezing": (
            "Sneezing is often a reaction to allergens or irritants. Try to identify potential allergens "
            "and avoid exposure. If symptoms persist, consider allergy testing."
        ),
        "wheezing": (
            "Wheezing could be a sign of asthma, respiratory infection, or airway irritation. "
            "See a doctor if wheezing occurs frequently or alongside shortness of breath."
        ),
    },
    "gastrointestinal": {
        "nausea": (
            "Nausea can result from infections, food sensitivities, or digestive issues. "
            "Stay hydrated, avoid heavy foods, and rest. If nausea persists, see a healthcare provider."
        ),
        "vomiting": (
            "Vomiting may indicate a gastrointestinal issue or infection. Stay hydrated with small sips of water. "
            "Seek medical advice if vomiting continues or if dehydration occurs."
        ),
        "diarrhea": (
            "Diarrhea can be due to infections, food poisoning, or dietary issues. Stay hydrated, "
            "and avoid fatty foods. Consult a doctor if it lasts more than two days."
        ),
        "constipation": (
            "Constipation can result from a low-fiber diet, dehydration, or lack of exercise. "
            "Increase fiber intake, drink water, and consider mild physical activity. "
            "Consult a doctor if it persists."
        ),
        "abdominal pain": (
            "Abdominal pain may result from digestive issues, infection, or muscle strain. "
            "Rest and avoid heavy meals. Seek medical advice if pain is intense or persistent."
        ),
    },
    "musculoskeletal": {
        "joint pain": (
            "Joint pain may be caused by arthritis, injury, or overuse. Rest the joint, apply ice, and avoid strenuous activity. "
            "If pain continues, consult a doctor."
        ),
        "muscle pain": (
            "Muscle pain is often due to strain or injury. Rest, hydrate, and consider light stretching if it’s mild. "
            "If pain persists, seek medical evaluation."
        ),
        "back pain": (
            "Back pain may arise from poor posture, strain, or underlying issues. Practice good posture, avoid lifting heavy objects, "
            "and see a doctor if it doesn’t improve."
        ),
        "neck pain": (
            "Neck pain can result from strain, poor posture, or injury. Rest and avoid sudden movements. "
            "Consult a doctor if it persists or is severe."
        ),
        "sprain": (
            "A sprain may require rest, ice, compression, and elevation (RICE). Avoid putting weight on the injured area, "
            "and consult a doctor if swelling or pain persists."
        ),
    },
    "neurological": {
        "headache": (
            "Headaches can stem from stress, dehydration, or other factors. Drink water, rest, and reduce screen time. "
            "Seek medical advice if headaches are frequent or severe."
        ),
        "dizziness": (
            "Dizziness may be due to dehydration, low blood pressure, or an inner ear issue. Sit or lie down, drink water, "
            "and if dizziness persists, consult a doctor."
        ),
        "tingling": (
            "Tingling may be caused by nerve irritation, circulation issues, or pressure on nerves. "
            "If tingling persists or affects a large area, seek medical advice."
        ),
        "numbness": (
            "Numbness can result from nerve compression, injury, or circulation issues. "
            "If numbness is persistent or extensive, consult a healthcare provider."
        ),
        "blurred vision": (
            "Blurred vision can occur from eye strain, fatigue, or other conditions. Rest your eyes and ensure good lighting. "
            "Seek medical advice if it persists or if you experience additional symptoms."
        ),
    },
    # Add more categories here, such as Cardiovascular, Dermatological, Immunological, etc.
}

def diagnose_symptoms(symptom):
    # Normalize the symptom input
    symptom = symptom.lower()
    # Search through categories and symptoms
    for category, symptoms in symptom_responses.items():
        if symptom in symptoms:
            return symptoms[symptom]
    return "Symptom not recognized. Please provide more details or consult a healthcare provider."

