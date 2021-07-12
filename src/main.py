### Program for adding English subtitles to a Russian video
import sys

# from model import CLASS

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

# Open file in first argument
with open(sys.argv[1], 'r') as video_file:
    # put video file as input to model
    output = model(video_file)

# Create .srt from model output
# Output should be a file in .srt format
