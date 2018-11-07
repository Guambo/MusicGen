import argparse
import random
from midiutil import MIDIFile
import os.path
#This version will generate random notes within a chord pogression, one bar, 2-8 chords chosen, 1 root note played in bass line
def generate(filename):
    # generate
    Key = random.randint(0,11)

    upper = 6
    lower = 5
    Mchords = generateChords()

    #degrees  = generateNotes(lower, upper, random.randint(0, 501), Key) # This is where the actual notes are stored ... ex: [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number

    track    = 0	# Literally, the track at which the notes are stored
    channel  = 0	# 1 = mono, 2 = stereo
    time     = 0    # When the note is played (the beat at which the note is played)
    duration = 1    # 1 = quarter note, 1/2 = eigth note
    tempo    = random.randint(80, 160)   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)

    MyMIDI.addTempo(track, time, tempo)
	# Idea: every iteration of the for loop, you randomly generate a new number
    for j in range(0,len(Mchords),1):
        cDegrees = generateCNotes(lower, upper, 8, Key, Mchords[j])
        baseNote = generateSNotes(3, 4, 8, Key, Mchords[j], 0)
        sDegrees = generateSNotes(3, 4, 8, Key, Mchords[j], 0)
        noteAdder(track, channel, j, 1, volume, cDegrees, MyMIDI)
        noteAdder(track, channel, j, 1, volume, baseNote, MyMIDI)
	# If we want to add more notes to track 0 then we can do this:
	# MyMIDI.addNote(track, channel, 60, time + 7, duration*0.5, volume-10)

    with open(filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)
# This function will generate a random sequence of notes (midi notes) and will return an array of random notes given certain constraints
def noteAdder(track, channel, j, duration, volume, notes, midi):
    for i, pitch in enumerate(notes):
        midi.addNote(track, channel, pitch, i+(j*8), duration, volume)# This is where we can configure the timing of each notev
def generateChords():
    Chordamt = random.randint(2,4)#Number of Chords In Chord Pogressio
    chordlist = Chords() #list of chords in Key
    retval = [0]*Chordamt
    for i in range(0,Chordamt,1):
        whichChord = random.randint(0,len(chordlist)-1)
        retval[i] = chordlist[whichChord]
        print(retval[i])
    return retval
def Chords():
    one = [0, 4, 7]
    two = [2, 5, 9]
    three = [4, 7, 11]
    majthree = [4, 8, 11]
    four = [5, 9, 0]
    minfour = [5, 8, 0]
    five = [7, 11, 2]
    six = [9, 0, 4]
    seven = [11, 2, 5]
    return [one,two,three,majthree,four,minfour,five,six,seven]
    #return [one,two,three,four,five,six]
def generateSNotes(lowerBound, upperBound, totalNotes, key, chord, degree):
#retval = [60, 62, 64, 65, 67, 69, 71, 72]
    retval = [0] * totalNotes # Randomly instantiates an array of size totalNotes
    for i in range(len(retval)):
        retval[i] = chord[degree]+12*random.randint(lowerBound, upperBound) + key

    return retval
def generateCNotes(lowerBound, upperBound, totalNotes, key, chord):
#retval = [60, 62, 64, 65, 67, 69, 71, 72]
    retval = [0] * totalNotes # Randomly instantiates an array of size totalNotes
    for i in range(len(retval)):
        degree = random.randint(0,2)
        retval[i] = chord[degree]+12*random.randint(lowerBound, upperBound) + key

    return retval

def play(filename):
    # play file
    print("playing file " + filename + "\n")

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--generate", dest = "path", help = "generate a MIDI file and write it out to PATH")

    args = parser.parse_args()

    if(type(args.path) is str):
        generate(args.path)
    elif(type(args.path) is int):
        generate(str(args.path))
    else:
        print("Bad command line arguments or none specified. Use the flag -h or --help to see a list of available flags to use with MusicGen.")
    main2()
def main2():
    save_path = 'D:/GithubRepos/MusicGen/'
    fileName = os.path.join(save_path, "test.mid")
    generate(fileName)
main2()
