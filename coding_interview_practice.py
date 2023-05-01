#Estimating File Sizes - www.101computing.net/file-size-calculations
'''This program calculates the file size of certain files including sound, text, and picture files'''
def estimateTextFileSize(bits_per_char, num_chars):
    # Multiplying to find how many bits
    
    bits = bits_per_char * num_chars
    if bits > 8000000:
        # Checking to see if file is over at least 1 MB
        mb = bits / 8000000
    
        return f'{round(mb,1)}MB'
    
    else:
        # If not then default to KB
        kb = bits / 8000
        return f'{round(kb,1)}KB'

def estimatePictureFileSize(width, heighth, depth):
    # Multiplying to find how many bits
    bits = width * heighth * depth
    if bits > 8000000:
        # Checking to see if file is over at least 1 MB
        mb = bits / 8000000
        return f'{round(mb,1)}MB'
    
    else:
        # If not then default to KB
        kb = bits / 8000
        return f'{round(kb,1)}KB'
    

def estimateSoundFileSize(s_rate, depth, duration, num_of_channels):
    # Multiplying to find how many bits
    bits = s_rate * depth * duration * num_of_channels
    if bits > 8000000:
        # Checking to see if file is over at least 1 MB
        mb = bits / 8000000
        return f'{round(mb,1)}KB'
    
    else:
        # If not then default to KB
        kb = bits / 8000
        return f'{round(kb,2)}MB'


def estimateGifFileSize(width, height, color, frame_rate, duration):
    # Multiplying to find how many bits
    bits = width * height * color * frame_rate * duration
    if bits > 8000000:
        # Checking to see if file is over at least 1 MB
        mb = bits / 8000000
        return f'{round(mb,1)}KB'
    
    else:
        # If not then default to KB
        kb = bits / 8000
        return f'{round(kb,2)}MB'
    

# def estimateMovieFileSize(width, height, color, frame_rate, duration, sample_rate, bit_depth, ):
#     # Multiplying to find how many bits
#     bits = width * height * color * frame_rate * duration
#     if bits > 8000000:
#         # Checking to see if file is over at least 1 MB
#         mb = bits / 8000000
#         return f'{round(mb,1)}KB'
    
#     else:
#         # If not then default to KB
#         kb = bits / 8000
#         return f'{round(kb,2)}MB'
# Width: 1920 pixels
# Height: 1080 pixels
# Colour depth: 24 bits
# Frame Rate: 24 fps
# Duration: 1 hour 15 minutes

# Soundtrack:
# Sample Rate: 48 KHZ
# Bit Depth: 16-bits per sample
# Duration: 1 hour 15 minutes.
# Channel: 6 (Dolby-Surround)

def input_for_text_file():
    # Checking input making sure they're numbers and making the calculation
    while True:
        try:
            bits_per_char = float(input("Please enter the number of bits per character: "))
            num_char = float(input("please enter the number of characters in text file: "))
            # Calling the estimateTextFileSize function to find size
            size = estimateTextFileSize(bits_per_char, num_char)
            print("This text file is", size, "big")
            print()
            break
        except ValueError:
            # Print an error if not an int
            print("Please enter a valid number")
            print()

def input_for_sound_file():
    # Same thing as input_for_text_file but for sound file
    while True:
        try:
            s_rate = float(input("Please enter the sample rate in KHZ: "))
            bit_depth = float(input("please enter the bit depth: "))
            duration = float(input("Please enter the duration in seconds: "))
            channels = int(input("Please enter how many channels: "))
            # Calling the estimateSoundFileSize function to find size
            size = estimateSoundFileSize(s_rate, bit_depth, duration, channels)
            print("This sound file is", size, "big")
            print()
            break
        except ValueError:
            # Print an error if not an int
            print("Please enter a valid number")
            print()



def input_for_pic_file():
    # Same thing as sound file but for pic file
    while True:
        try:
            width = int(input("Please enter width in pixels: "))
            heighth = int(input("please enter heighth in pixels: "))
            color_depth = int(input("Please enter color depth: "))
            # Calling estimatePictureFileSize
            size = estimatePictureFileSize(width, heighth, color_depth)
            print("This picture file is", size, "big")
            print()
            break
        except ValueError:
            # Print error if not an int
            print("Please enter a valid number")
            print() 

def main():
    # Main function to run everything
    while True:
        # While loop to run until user presses 'q'
        print("Please enter a number corresponding the type of file you want the size of:")
        print("1.) Text file")
        print("2.) Sound file")
        print("3.) Picture file ")
        user_input = input("Enter a number or press 'q' to exit: ")

        if user_input.lower() == "q":
            break

        elif user_input == '1':
            input_for_text_file()

        elif user_input == '2':
            input_for_sound_file()

        elif user_input == '3':
            input_for_pic_file()

        elif user_input == '4':

        elif user_input == '5':

        else: 
            print("Please enter 1, 2, 3, or 'q'")
            print()

if __name__ == "__main__":
    # Calls main function
    main()