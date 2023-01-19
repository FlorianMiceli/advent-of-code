fileinput = open('input 06.txt', 'r')
datastream = fileinput.readlines()
datastream = datastream[0]

# if 4 bytes are unique consecutively, return the index+1
def find_start_of_packet(datastream):

    for i in range(3,len(datastream)):

        current_bytes = datastream[i-3:i+1]
        nbr_of_unique_bytes = 0

        k = 0
        for byte in current_bytes:

            if byte not in current_bytes[:k]+current_bytes[k+1:] :
                nbr_of_unique_bytes += 1
            k += 1
        
        if nbr_of_unique_bytes == 4:
            return i+1

# if 14 bytes are unique consecutively, return the index+1
def find_start_of_message(datastream):
    
        for i in range(13,len(datastream)):
    
            current_bytes = datastream[i-13:i+1]
            nbr_of_unique_bytes = 0
    
            k = 0
            for byte in current_bytes:
    
                if byte not in current_bytes[:k]+current_bytes[k+1:] :
                    nbr_of_unique_bytes += 1
                k += 1
            
            if nbr_of_unique_bytes == 14:
                return i+1



print('first packet marker after caracter :',find_start_of_packet(datastream))
print('first message marker after caracter :',find_start_of_message(datastream))