import argparse
from midiutil import MIDIFile

def generate(filename):
    # generate
    degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                          # automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

    with open(filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)


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
