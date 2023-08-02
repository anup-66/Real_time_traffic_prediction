
# import xmltodict
# import json
#
# # XML input string
# xml_input = '''
# <root>
#     <person>
#         <name>John Doe</name>
#         <age>30</age>
#         <city>New York</city>
#     </person>
#     <person>
#         <name>Jane Smith</name>
#         <age>25</age>
#         <city>Los Angeles</city>
#     </person>
# </root>
# '''
#
# # Convert XML to OrderedDict
# # xml_dict = xmltodict.parse(xml_content)
# #
# # # Convert OrderedDict to JSON
# # json_output = json.dumps(xml_dict)
# # with open("json_data.json","w") as f:
# #     f.write(json_output)
# # # Output the JSON
# # print(json_output)
# import librosa
# import librosa.display
# import matplotlib.pyplot as plt
# #
# # # Load the audio file
# audio_path = "C:\\Users\\Anup\\Downloads\\mixkit-orchestral-christmas-happy-music-2987.wav"
# # audio, sr = librosa.load(audio_path)
# #
# # # Extract MFCCs
# # mfccs = librosa.feature.mfcc(y = audio, sr=sr)
# #
# # # Plot MFCCs
# # plt.figure(figsize=(10, 4))
# # librosa.display.specshow(mfccs, x_axis='time')
# # plt.colorbar(format='%+2.0f dB')
# # plt.title('MFCCs')
# # plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# import librosa
#
# # Load the audio file
# # audio_path = 'path/to/audio/file.wav'
# audio, sr = librosa.load(audio_path)
#
# # Calculate the one-dimensional FFT
# fft = np.fft.fft(audio)
#
# # Calculate the magnitude spectrum
# magnitude = np.abs(fft)
#
# # Create the frequency axis
# frequency = np.linspace(0, sr, len(magnitude))
#
# # Plot the frequency spectrum
# # plt.plot(frequency, magnitude)
# # plt.xlabel('Frequency (Hz)')
# # plt.ylabel('Magnitude')
# # plt.title('Frequency Spectrum')
# # plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# import librosa
#
# # Load the audio file
# # audio_path = 'path/to/audio/file.wav'
# audio, sr = librosa.load(audio_path)
#
# # Calculate the one-dimensional FFT
# fft = np.fft.fft(audio)
#
# # Calculate the magnitude spectrum
# magnitude = np.abs(fft)
#
# # Create the frequency axis
# frequency = np.linspace(0, sr, len(magnitude))
#
# # Define the range of frequencies to plot (e.g., middle 50%)
# freq_min = 0.25 * sr
# freq_max = 0.75 * sr
# index_min = int(freq_min * len(magnitude) / sr)
# index_max = int(freq_max * len(magnitude) / sr)
#
# # Subset the frequency and magnitude arrays
# frequency_subset = frequency[index_min:index_max]
# magnitude_subset = magnitude[index_min:index_max]
#
# # Plot the frequency spectrum subset
# plt.plot(frequency_subset, magnitude_subset)
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('Frequency Spectrum (Middle Frequencies)')
# # plt.show()
#
# import matplotlib.pyplot as plt
# import librosa
# import librosa.display
#
# # Load the audio file
# # audio_path = 'path/to/audio/file.wav'
# audio, sr = librosa.load(audio_path)
#
# # Generate the waveform plot
# plt.figure(figsize=(10, 4))
# print(librosa.display.waveshow(y = audio, sr=sr))
# # plt.xlabel('Time (s)')
# # plt.ylabel('Amplitude')
# plt.axis('off')
# plt.tight_layout()
# plt.title('Waveform')
# plt.show()
#
# a = [1,2,3]
# # b = [4,5,6]
# # print(a + b)
# weeks = list()
# # fname = input('Enter File ')
# # if len(fname) < 1: fname = 'file.txt'
# hand = open("file.txt")
# di = dict()
# for lin in hand:
#     lin = lin.rstrip()
#     print(lin)
#     wds = lin.split()
# for w in wds:
#     di[w] = di.get(w,0) + 1
#     largest = -1
# theword = None
# for k,v in di.items():
#     print(k,v)
#     if v > largest :
#         largest = v
#         theword = k
# print(v,k)
inp = input("Enter the file name : ")
with open(inp,"r") as f:
    Str = f.read().strip().split()
    Dict = {}
    for i in Str:
        Dict[i] = Dict.get(i,0) + 1
for Key,value in Dict.items():
    print(Key,value,end = ' ')