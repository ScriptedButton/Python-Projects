from io import SEEK_CUR

class ImageHandler:
    def __init__(self):
        self.option = ""
    def main(self, image, effect):
        self.option = effect
        imgFile = open(image, "rb+")

        # Extract the image information.
        fileSize = self.readInt(imgFile, 2)
        start = self.readInt(imgFile, 10)
        width = self.readInt(imgFile, 18)
        height = self.readInt(imgFile, 22)

        # Scan lines must occupy multiples of four bytes.
        scanlineSize = width * 3
        if scanlineSize % 4 == 0:
            padding = 0
        else:
            padding = 4 - scanlineSize % 4

        # Make sure this is a valid image.
        if fileSize != (start + (scanlineSize + padding) * height):
            exit("Not a 24-bit true color image file.")

        # Move to the first pixel in the image.
        imgFile.seek(start)

        # Process the individual pixels.
        for row in range(height):  # For each scan line
            for col in range(width):  # For each pixel in the line
                self.processPixel(imgFile)

                # Skip the padding at the end
            imgFile.seek(padding, SEEK_CUR)

        imgFile.close()

        ## Processes an individual pixel.

    #  @param imgFile the binary file containing the BMP image
    #
    def processPixel(self, imgFile):
        # Read the pixel as individual bytes.
        theBytes = imgFile.read(3)
        blue = theBytes[0]
        green = theBytes[1]
        red = theBytes[2]
        if self.option == "sunset":
            newBlue = int(blue * .30)
            newGreen = int(green * .30)
            newRed = red
        elif self.option == "grayscale":
            gray = int(blue * .11 + green * .59 + red * .30)
            newBlue = gray
            newGreen = gray
            newRed = gray
        # Process the pixel.

        # Write the pixel.
        imgFile.seek(-3, SEEK_CUR)  # Go back 3 bytes to the start of the pixel
        imgFile.write(bytes([newBlue, newGreen, newRed]))

    ## Gets an integer from a binary file.
    #  @param imgFile the file
    #  @param offset the offset at which to read the integer
    #  @return the integer starting at the given offset
    #
    def readInt(self, imgFile, offset):
        # Move the file pointer to the given byte within the file.
        imgFile.seek(offset)

        # Read the 4 individual bytes and build an integer.
        theBytes = imgFile.read(4)
        result = 0
        base = 1
        for i in range(4):
            result = result + theBytes[i] * base
            base = base * 256

        return result


##
#  This program processes a digital image by creating a negative of a BMP image.
#


# Start the program.

ih = ImageHandler()

file = input("Choose a file: ")
print("Effects: sunset, grayscale" + "\n")
effect = input("Choose an effect: ")
if effect != "sunset" and effect != "grayscale":
    print("Invalid effect!")
else:
    try:
        ih.main(file, effect)
    except FileNotFoundError:
        print("Invalid file!")
