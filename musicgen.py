import argparse
import random
from midiutil import MIDIFile

def generate(filename):
    # generate
    degrees  = generateNotes(1, 60, 8) # This is where the actual notes are stored ... ex: [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
    track    = 0	# Literally, the track at which the notes are stored
    channel  = 0	# 1 = mono, 2 = stereo
    time     = 0    # When the note is played (the beat at which the note is played)
    duration = 1    # 1 = quarter note, 1/2 = eigth note
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                          # automatically)
    MyMIDI.addTempo(track, time, tempo)
	# Idea: every iteration of the for loop, you randomly generate a new number
    for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, time + i*0.5, duration * 1/2, volume) # This is where we can configure the timing of each note

	# If we want to add more notes to track 0 then we can do this:
	# MyMIDI.addNote(track, channel, 60, time + 7, duration*0.5, volume-10)

    with open(filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)

# This function will generate a random sequence of notes (midi notes) and will return an array of random notes given certain constraints
def generateNotes(lowerBound, upperBound, totalNotes):
	#retval = [60, 62, 64, 65, 67, 69, 71, 72]
	retval = [0] * totalNotes # Randomly instantiates an array of size totalNotes
	for i in retval:
		i = random.randint(lowerBound, upperBound)

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

main()
