def chakr_chat(user_input):
    greet =['hi', 'hello', 'hey', 'greetings', 'chakr', 'chat']
    bid = ['bye', 'thank you', 'thanks']
    relief_str = ['relief', 'camp', 'food', 'stay']
    help_str = ['help', 'ndrf', 'save']
    insurance_str = ['insurance', 'money', 'claim']
    updates_str = ['update', 'updates', 'news', 'today']
    train_str = ['train', 'railway', 'cancel']

    user_input = user_input.lower()

    text = user_input.split()
    
    for i in text:
        if i in greet:
            return 'Chakr-Chat activated. How can I help You?'
        
        elif i in relief_str:
            file = open('text.txt')
            content = file.readlines()

            print('Chakr-Chat: Enter your ward number') 
            ward = int(input('You: '))
            if 0<ward<10:
                for i in range(0,10):
                    if content[i][0]== str(ward):
                        return 'Ward Number', content[i].rstrip('\n')
            
            elif 9<ward:
                for i in range(0,43):
                    if content[i][0:2] == str(ward):
                        return 'Ward Number', content[i].rstrip('\n')
        
        elif i in help_str:

            print('Chakr-Chat: State Disaster Manangement Authority Helpline: 1070')
            print('Chakr-Chat: Whatsapp: 9445869848')
            print('Chakr-Chat: NDRF Helpline Number: +91-9711077372')
            file = open('help.txt')
            content = file.readlines()

            print('Chakr-Chat: Enter your pincode') 
            pin = (input('You: '))
            for i in range(0,13):
                if content[i][0:6] == (pin):
                    return 'Pin Code', content[i].rstrip('\n')

                
        elif i in insurance_str:
            

            print('Chakr-Chat: Flood-damaged vehicles are covered under motor insurance policies. Claims can be made for own damage, third-party liability, and total loss.')
            print('Chakr-Chat: Enter your insurance company')
            comp = input('You: ')

            if 'icici' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Report. Once reported, you\'ll be assigned a dedicated Claim Manager.', 'Provide approval to the Claim Assessment', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document lose, please type RELIEF. For more: 1800 2666'
            
            elif 'acko' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Raise claim through Acko app', 'Your vehicle will be collected', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement', 'Original Purchase Invoice',sep ='\n')
                return 'In case of document lose, please type RELIEF. For more: 1800 266 2256'
    
            elif 'sundaram' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Inform about the claim. You\'ll be contacted by them further', sep = '\n')
                print('Chakr-Chat: Documents Required','Claim Form','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document lose, please type RELIEF. For more: 18005689999'
            
            elif 'cholamandalam' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Request for Claim Intiation', 'INspection', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document lose, please type RELIEF. For more: 1800 208 5544'
            
            elif 'hdfc' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Register claim', 'Wait for claim approval', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document lose, please type RELIEF. For more: 022 6234 6234'
            
            else:
                return 'The company is not yet associated with Chakr-Chat. I recommend visiting their website.'
            
        elif i in updates_str:
            return 'I can not provide real time data as per my latest update. Stay Safe'
        
        
        elif i in updates_str:
            return 'I can not provide real time data as per my latest update. Stay Safe'
            
        elif i in bid:
            return 'Thank You for being with Chakr-Chat. Be Safe!'


def main():
    while True:
        user_input = input('You: ')

        response = chakr_chat(user_input)
        print('Chakr-Chat:', response)

if __name__ == '__main__': #__name__ built-in python variable, when script is executed __name__ is set to __main__ by default
    main() 
