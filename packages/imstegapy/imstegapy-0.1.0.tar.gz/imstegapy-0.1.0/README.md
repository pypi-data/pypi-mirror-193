# Imsteg
An image steganography tool used for hiding text inside images made as a hobby project.

# Installation
```
pip install imstegapy
```

# Example Usage
```py
import imsteg

codec = imsteg.StegCodec()

img = codec.encode("path/to/file.png", "text here")
img.save("imagename.png")  # only pngs seems to work properly.

print(codec.decode("imagename.png"))
>>> text here