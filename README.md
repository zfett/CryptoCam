# CryptoCam
_Generate pseudo-random values using live camera input._
***
### __⚠️ DO NOT USE THE VALUES RETURNED FROM THIS PROGRAM FOR CRYPTOGRAPHIC KEY GENERATION! ⚠️__
***
## About
CryptoCam is a simple Python program that takes a photo from your computer's primary camera and generates a sha256 checksum from its data. This checksum can then be used for pseudo-random number generation.

## How?
By using OpenCV for Python and hashlib, CryptoCam takes a photo from your primary camera device and saves it to the path specified in the `PHOTO_PATH` constant as a `.png` file. Next, using hashlib, CryptoCam generates a sha256 checksum from the photo's binary data and saves it to the path specified in the `HASH_PATH` constant, or returns the value without saving a file if you specify the `saveToFile` arg as `"false"` on the `generateHash()` function.

## Why?
I dunno, it's was a fun little sideproject for me! I've always wanted to get a Raspberry Pi for little programming projects but I've never had any ideas what to run on it, now I do!

## Installation
To "install" CryptoCam, first clone this repo to your directory of choice, then make sure to install OpenCV for Python by running `pip3 install opencv-python` on your command line. Once you've installed OpenCV, you then run the program by simply including the module like this:

```
import cryptocam as cc

cc.generateHash("true", "checksum.txt", "capture.png")
```

## Usage
- `generateHash(saveToFile, hashPath, photoPath)` - Used to generate the checksum from the photo data.
  - Arguments:
    - `saveToFile` [`"true"` | `"false"`] - If `"true"`, then saves the checksum value to a file defined in the `hashPath` arg.
    - `hashPath` [string to path] - Defines the save path and filename for the checksum value if `saveToFile` is `"true"`.
      - _Example:_ `generateHash("true", "src/checksum.txt", ...)`
    - `photoPath` [string to path] - Defines the save path and filename for the photo capture. Must end with `.png`. Cannot be blank.
      - _Example:_ `generateHash("true", "src/checksum.txt", "src/capture.png")`

## License
CryptoCam is licensed under the GNU GPLv3 license. To learn more about this license, please reference the full text in the `LICENSE` file at the root of this repository.