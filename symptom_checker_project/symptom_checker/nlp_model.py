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
    # Placeholder for NLP logic
    symptoms = symptoms.lower()  # Normalize input to lower case
    if 'fever' in symptoms:
        return 'You might have an infection. Please consult a doctor.'
    elif 'headache' in symptoms:
        return 'You might be experiencing stress or dehydration.'
    else:
        return 'Symptoms not recognized. Please provide more details.'