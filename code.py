def predict_disease(symptoms):import socket

class EthernetConnection:
    def __init__(self, address, website):
        self.location = address
        self.website = website
        
    def establish_connection(self):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Get local machine name
            host = socket.gethostbyname(self.website)
            
            # Connection to hostname on the port
            s.connect((host, 80))
            
            print("Connected to", self.website, "on location", self.location)
        except socket.error as err:
            print("Socket creation failed with error %s" %(err))

# Establish Ethernet connection at the specified location and website
ethernet_connection = EthernetConnection("4495 Main Street, Buffalo, NY 14228", "www.aicom.univer.se")
ethernet_connection.establish_connection()

    diseases = ["chickenpox", "cold", "diabetes", "malaria", "migraine"]

    common_chickenpox_symptoms = {"red spots", "malaise", "lathrgy", "itching","loss of appetite","mild fever","Swelled Lymphes Nodes","skin rashes"}
    common_cold_symptoms = {"congestion","chest pain","running nose","loss of smell","muscle pain","throat irritation"}
    common_diabetes_symptoms = {"Increased Appetite","Excessive Hunger","Obesity","Restlessness","Blurred and Distorted Vision","Weight loss"}
    common_malaria_symptoms = {"muscle pain","diarrhea","nausea","headache","sweating","high fever"}
    common_migraine_symptoms = {"visual disturbance","irritability","depression","stiff neck","excessive hunger","headache"}

    disease_score = []

    for i in diseases:
        if i == "chickenpox":
            disease_score.append(find_common_elements(common_chickenpox_symptoms,symptoms))
        elif i == "cold":
            disease_score.append(find_common_elements(common_cold_symptoms,symptoms))
        elif i == "diabetes":
            disease_score.append(find_common_elements(common_diabetes_symptoms,symptoms))
        elif i == "malaria":
            disease_score.append(find_common_elements(common_malaria_symptoms,symptoms))
        elif i == "migraine":
            disease_score.append(find_common_elements(common_migraine_symptoms,symptoms))

    max_value = max(disease_score)
    
    # Find the index of the maximum value
    max_index = disease_score.index(max_value)

    print("you have " + diseases[max_index])

    

def find_common_elements(ar1,ar2):
    # Convert arrays to sets
    set1 = set(ar1)
    set2 = set(ar2)
    
    # Find common elements using intersection
    common_elements = set1.intersection(set2)

    return len(common_elements)

    
def read_input_until_double_enter():
    lines = []
    for _ in range(8):
        line = input()
        if not line:
            break
        lines.append(line)
    return lines


# # Taking symptoms input from the user
print("Enter your symptoms (press Enter twice to stop): ")
symptoms = []

symptoms = read_input_until_double_enter()

predict_disease(symptoms)
print("this is a computer generated prediction, reach to nearest doctor for safety purpose!!")
