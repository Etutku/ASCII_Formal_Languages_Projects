# Introduction to the ASCII Video Converter
The ASCII Code Video project is an innovative exploration at the intersection of technology and art, leveraging the power of p5.js to transform ordinary video footage into ASCII in real-time. Basically, it turns video (pixel) format into binary (01) or **ASCII** characters. 

If we consider similarity with formal languages, the project demonstrates a connection through its underlying principles of language representation and transformation. While the project itself may not involve a traditional compiler in the sense of translating high-level programming languages into machine code, it exhibits certain similarities and connections.

**Similarity**: In formal languages and compilers, there is a focus on the representation of information and the transformation of one form of language into another. ASCII Code Video represents video frames through the language of ASCII characters, showcasing a transformation from pixel-based images to character-based representation. As in the summary we can say that it converts pixel(s) to characters. 

## Key Features
- **Real-time ASCII Art:**  `p5.js` sketch processes video frames, creating a captivating ASCII representation that evolves with the video content.

- **Customization:** The project is designed to be customizable. Users can experiment with different character sets, fonts, and video processing parameters to achievwe results.

- **Easy Integration:** With a straightforward setup and intuitive interface, users can quickly run the project locally and experience the beauty of ASCII  videos in their **web browser**.

## Explaining Code and Steps
Project is mainly done with JavaScript and p5.js,  to transform ordinary video footage into mesmerizing ASCII art in real-time. In the repository there are 3 main files, one of them is sketch.js (main file) and the other one is style.css for design the project. Analyzing the sketch.js:

* const density = "Ñ@#W$9876543210?!abc;:+=-,.”;   // This code block matches pixels with **ASCII characters**, and they can be changeable to binary too.
* const density = "01”;   // This code block will convert **pixels** into **binary**.

  If we scroll further to the codes in sketch.js, this part will be help to get RGB pixel data and convert it to the density (const density) that we assigned in the beginning:

  ```javascript
  const r = video.pixels[pixelIndex + 0];
  const g = video.pixels[pixelIndex + 1];
  const b = video.pixels[pixelIndex + 2];
  const avg = (r + g + b) / 3;
  const len = density.length;
  const charIndex = floor(map(avg, 0, 255, 0, len));
  const c = density.charAt(charIndex);

## Running the Program
For running the program, sketch.js has to be compiled with the browser (it can be Safari, Chrome etc.) and it will need permission from the camera. Then, with the camera there will be visualization with RGB pixels, and on the other side of the program ASCII character conversion will appear. 
