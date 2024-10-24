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


def diagnose_symptoms(symptoms):
    # Normalize input to lower case
    symptoms = symptoms.lower()
    
    if 'fever' in symptoms:
        return 'You might have an infection. Please consult a doctor.'
    elif 'headache' in symptoms:
        return 'You might be experiencing stress or dehydration.'
    elif 'cough' in symptoms:
        return 'You may have a respiratory infection or allergies. Consider seeing a doctor if it persists.'
    elif 'sore throat' in symptoms:
        return 'This could indicate a throat infection or allergies. Please consult a healthcare professional.'
    elif 'muscle pain' in symptoms:
        return 'You might be experiencing muscle strain or overexertion. Rest and hydration are recommended.'
    elif 'joint pain' in symptoms:
        return 'This could be a sign of arthritis or an injury. Please consult a doctor for a proper diagnosis.'
    elif 'sprain' in symptoms:
        return 'A sprain may require rest, ice, compression, and elevation (RICE). Consult a doctor if pain persists.'
    elif 'fracture' in symptoms:
        return 'If you suspect a fracture, please seek immediate medical attention.'
    elif 'back pain' in symptoms:
        return 'Back pain can result from various issues, including muscle strain or herniated discs. Consider consulting a doctor.'
    elif 'nausea' in symptoms:
        return 'Nausea can be caused by various factors, including infections or gastrointestinal issues. Please consult a doctor if it persists.'
    else:
        return 'Symptoms not recognized. Please provide more details.'