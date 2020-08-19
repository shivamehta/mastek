import keras
import os
import numpy as np
import librosa
import matplotlib.pyplot as plt
import glob
import os.path
import speech_recognition as sr
import pydub
from pydub import AudioSegment
from pydub.utils import make_chunks
import nltk
import datetime
from difflib import SequenceMatcher
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sys
import tkinter as tk
import tkinter.ttk as ttk
from scipy.io import wavfile
import wave
from dicttoxml import dicttoxml
import re
import subprocess, sys

r="A"

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("999x254+435+139")
        top.title("Interaction Analysis")
        top.configure(background="#1A5276")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.541, rely=0.472, height=33, width=106)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#99A3A4")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Browse''', command=self.load_file)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.731, rely=0.709, height=33, width=206)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#99A3A4")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Emotional Analysis''', command = self.emotionAnalyse)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.08, rely=0.709, height=33, width=206)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#99A3A4")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Speech to Text''', command=self.STT)
        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.23, rely=0.63, relwidth=0.551)

        self.Button3_2 = tk.Button(top)
        self.Button3_2.place(relx=0.41, rely=0.709, height=33, width=206)
        self.Button3_2.configure(activebackground="#ececec")
        self.Button3_2.configure(activeforeground="#000000")
        self.Button3_2.configure(background="#99A3A4")
        self.Button3_2.configure(disabledforeground="#a3a3a3")
        self.Button3_2.configure(foreground="#000000")
        self.Button3_2.configure(highlightbackground="#d9d9d9")
        self.Button3_2.configure(highlightcolor="black")
        self.Button3_2.configure(pady="0")
        self.Button3_2.configure(text='''Agent Analysis''',command=self.agentAnalysis)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.36, rely=0.472, height=26, width=182)
        self.Label1.configure(activebackground="#a4d8d6")
        self.Label1.configure(activeforeground="#a4d8d6")
        self.Label1.configure(background="#1A5276")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#a4d8d6")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Import Audio File''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.0, height=96, width=1001)
        self.Label2.configure(background="#3498DB")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text='''INTERACTION ANALYSIS OVER SPEECH FOR CALL CENTER OPTIMIZATION''')
        self.Label2.configure(width=1001)

    def load_file(self):
        fname = askopenfilename(filetypes=(("WAV files","*.wav"),("All files", "*.*")) )
        if fname:
            try:
                global r
                r=fname
                print(fname)
            except:                     
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return

    def STT(self):
        global r
        print (r)
        audioloc=os.path.dirname(r)
        print(audioloc)
        filename = (os.path.splitext(os.path.basename(r))[0])
        filenames=[]
        filenames = sorted(glob.glob(audioloc+"/"+filename+"*.wav"))
        os.chdir(audioloc)
        open('STToutput.txt', 'w').close()
        l=len(filenames)
        print(filenames)
        for i in range(0,l):
            wave_file=filenames[i]    
            print("Processing {}...".format(wave_file))
            frequency_sampling, audio_signal = wavfile.read(wave_file)
            print('Signal shape:', audio_signal.shape)
            print('Signal Datatype:', audio_signal.dtype)
            print('Signal duration:', round(audio_signal.shape[0] / 
            float(frequency_sampling), 2), 'seconds')
            
            audio_signal = audio_signal / np.power(2, 15)
            audio_signal = audio_signal [:100]
            
            time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling)
            
            plt.plot(time_axis, audio_signal, color='blue')
            plt.xlabel('Time (milliseconds)')
            plt.ylabel('Amplitude')
            plt.title('Input audio signal')
#            plt.show()
            
            #Transformation into Frequency Domain
            audio_signal = audio_signal / np.power(2, 15)
            
            length_signal = len(audio_signal)
            half_length = np.ceil((length_signal + 1) / 2.0).astype(np.int)
            signal_frequency = np.fft.fft(audio_signal)
            signal_frequency = abs(signal_frequency[0:half_length]) / length_signal
            signal_frequency **= 2
            len_fts = len(signal_frequency)
            
            if length_signal % 2:
               signal_frequency[1:len_fts] *= 2
            else:
               signal_frequency[1:len_fts-1] *= 2
            signal_power = 10 * np.log10(signal_frequency)
            x_axis = np.arange(0, len_fts, 1) * (frequency_sampling / length_signal) / 1000.0
            plt.figure()
            plt.plot(x_axis, signal_power, color='black')
            plt.xlabel('Frequency (kHz)')
            plt.ylabel('Signal power (dB)')
#            plt.show()
            
            
            #Feature Extraction from Speech -
            from python_speech_features import mfcc, logfbank
            frequency_sampling, audio_signal = wavfile.read(wave_file)
            audio_signal = audio_signal[:15000]
            features_mfcc = mfcc(audio_signal, frequency_sampling)
            print('\nMFCC:\nNumber of windows =', features_mfcc.shape[0])
            print('Length of each feature =', features_mfcc.shape[1])
            features_mfcc = features_mfcc.T
#            plt.matshow(features_mfcc)
            plt.title('MFCC')
            filterbank_features = logfbank(audio_signal, frequency_sampling)
            print('\nFilter bank:\nNumber of windows =', filterbank_features.shape[0])
            print('Length of each feature =', filterbank_features.shape[1])
            
            filterbank_features = filterbank_features.T
            plt.matshow(filterbank_features)
            plt.title('Filter bank')
#            plt.show()
            AUDIO_FILE = (wave_file) 
            t = sr.Recognizer() 
            with sr.AudioFile(AUDIO_FILE) as source: 
                audio = t.record(source) 
                value = t.recognize_google(audio)
                try: 
                    print("The audio file contains: " +value)
                except sr.UnknownValueError: 
                    print("Speech Recognition could not understand audio") 
                except sr.RequestError as e: 
                    print("Could not request results from Speech Recognition service; {0}".format(e)) 
            os.chdir(r"C:\\finalyear")
            Outfile=open("STToutput.txt", 'a+')
            Outfile.write(t.recognize_google(audio))
            Outfile.write('.')
            Outfile.close()

    def agentAnalysis(self):
            global r
            a = 1
            audioloc=os.path.dirname(r)
            print(audioloc)
            text =["Please Hold for a Moment","That’s our Policy","Idiot","Stupid","Bitch","Asshole","Just go to our Website","Thats the Manufacturers Responsibility","I dont Know","Thats not my Department","You will have to speak with", "Can I transfer your call?","I dont set the Company Policy","You did that Wrong","Ill have call you back in 5 minutes"] 
            greet=["Hello","Morning","GoodMorning","Welcome"]
            close=["Thank you","Goognight","Welcome","Niceday"]
            ps = PorterStemmer()
            f = open(r"C:\\finalyear\\STToutput.txt").read()
            words = word_tokenize(f)
            f1=f
            l=sent_tokenize(f1)
            WORD = re.compile(r'\w+')
            ###Repeating Sentences
            c=0
            for i in range(len(l)-2):
                    for j in range(i):
                            r=SequenceMatcher(None,l[j],l[i]).ratio()
                            if(r>0.65):
                                    c=c+1
                                    
            ###Banned words
            d=0
            def get_cosine(vec1, vec2):
                 intersection = set(vec1.keys()) & set(vec2.keys())
                 numerator = sum([vec1[x] * vec2[x] for x in intersection])

                 sum1 = sum([vec1[x]**2 for x in vec1.keys()])
                 sum2 = sum([vec2[x]**2 for x in vec2.keys()])
                 denominator = math.sqrt(sum1) * math.sqrt(sum2)

                 if not denominator:
                    return 0.0
                 else:
                    return float(numerator) / denominator

            def text_to_vector(text):
                 words = WORD.findall(text)
                 return Counter(words)

            for i in range(len(l)-1):
                    for j in range(len(text)-1):
                            vector1 = text_to_vector(l[i])
                            vector2 = text_to_vector(text[j])
                            cosine = get_cosine(vector1, vector2)
                            if(cosine>0.50):
                                    d=d+1

            #Greeting Score
            greetcount=0
            for i in range(len(words)-2):
                 for j in range(len(greet)):
                        r=SequenceMatcher(None,greet[j],words[i]).ratio()
                        if(r>0.85):
                                greetcount=greetcount+1
            date=datetime.datetime.now()
            if(greetcount>=1):
                greetscore=100
            else:
                greetscore=0

            #Closing Score
            closecount=0
            for i in range(len(words)-2):
                 for j in range(len(greet)):
                        r=SequenceMatcher(None,close[j],words[i]).ratio()
                        if(r>0.85):
                                closecount=closecount+1
            if(closecount>=1):
                closescore=100
            else:
                closescore=0

            D1={"Call ID":"1", "Banned Words":d, "Call Attempt":"Successful!", "Agent ID":1, "Repeating Sentences":c, "Date":date , "Greeting Score":greetscore, "Closing Score":closescore}
            xml=dicttoxml(D1)
            os.chdir(audioloc)
            #xml=xml.decode()
            xml
            '''<?xml version="1.0" encoding="UTF-8" ?>
            <root>&#13;&#10;
            <CallID>1</CallID>&#13;&#10;
            <BannedWords>d</BannedWords>&#13;&#10;
            <AgentID>aid</AgentID>&#13;&#10;
            <Repeating Sentences>c</Repeating Sentences>&#13;&#10;
            <Date>date</Date>&#13;&#10;
            <Greeting Score></Greeting Score>&#13;&#10;
            <Closing Score>closescore</Closing Score>&#13;&#10;
            </root>'''
            xmlfile=open("AgentAnalysis.xml","w")
            xmlfile.write(xml.decode())
            xmlfile.close()
            print("Agent Analysis completed")

    def emotionAnalyse(self):
        global r
        print (r)
        audioloc="A"
        audioloc=os.path.dirname(r)
        print(audioloc)
        filename = (os.path.splitext(os.path.basename(r))[0])
        print(filename)
        loaded_model = keras.models.load_model(r'C:\\finalyear\\Emotion_Voice_Detection_Model.h5')
        filenames=[]
        plotemotion = []
        plotx = []
        plotemotion.append("None")
        plotx.append(0)
        #making chunks
        myaudio = AudioSegment.from_file(r, "wav") 
        chunk_length_ms = 3000 # pydub calculates in millisec
        chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of three sec
        os.chdir(audioloc+"/")
        for i, chunk in enumerate(chunks):
            chunk_name = "chunk{0}.wav".format(i)
            print ("exporting", chunk_name)
            chunk.export(chunk_name, format="wav")

        filenames = sorted(glob.glob(audioloc+"\chunk*.wav"))
        l=len(filenames)
        print(filenames)
        c=1
        
        for i in range(0,l):
            wave_file=filenames[i]
            #loading into dataframe and predicition
            data, sampling_rate = librosa.load(wave_file)
            mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
            x = np.expand_dims(mfccs, axis=1)
            x = np.expand_dims(x, axis=0)
            predictions = loaded_model.predict_classes(x)
            #making predictions
            if predictions == 0:
                pred = "neutral"
            elif predictions == 1:
                pred = "calm"
            elif predictions == 2:
                pred = "happy"
            elif predictions == 3:
                pred = "sad"
            elif predictions == 4:
                pred = "angry"
            elif predictions == 5:
                pred = "angry"
            elif predictions == 6:
                pred = "disgust"
            elif predictions == 7:
                pred = "surprised"
            print(pred)
            plotemotion.append(pred)
            print(plotemotion)
            plott = 3*c
            plotx.append(plott)
            print(plotx)
            c=c+1

        plt.ylabel('Emotions')
        plt.xlabel('Customer speech time')
        plt.bar(plotx,plotemotion)
        plt.savefig('emotion.png')
        plt.show()

if __name__ == '__main__':
    vp_start_gui()
