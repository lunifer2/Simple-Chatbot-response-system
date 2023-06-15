import random
R_EATING = "I dont like eating anything because I am a chatbot"
R_INFO = "I'm afraid I don't have the information you're seeking. Is there anything else I can assist you with?"
R_GUIDANCE = 'I can certainly provide guidance on that topic. What would you like to know?'
R_ASK = 'Absolutely! Ask away and I will do my best to provide a helpful response.'
def unknown():
    response = ['Could you please re-phrase that?',
                "......",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    
    return response