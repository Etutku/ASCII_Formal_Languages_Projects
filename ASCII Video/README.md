# Introduction to the ASCII Video Converter
The ASCII Code Video project is an innovative exploration at the intersection of technology and art, leveraging the power of p5.js to transform ordinary video footage into ASCII in real-time. Basically, it turns video (pixel) format into binary (01) or **ASCII** characters. 

If we consider similarity with formal languages, the project demonstrates a connection through its underlying principles of language representation and transformation. While the project itself may not involve a traditional compiler in the sense of translating high-level programming languages into machine code, it exhibits certain similarities and connections.

**Similarity**: In formal languages and compilers, there is a focus on the representation of information and the transformation of one form of language into another. ASCII Code Video represents video frames through the language of ASCII characters, showcasing a transformation from pixel-based images to character-based representation. As in the summary we can say that it converts pixel(s) to characters. 

## Key Features
- **Real-time ASCII Art:**  `p5.js` sketch processes video frames, creating a captivating ASCII representation that evolves with the video content.

- **Customization:** The project is designed to be customizable. Users can experiment with different character sets, fonts, and video processing parameters to achievwe results.

- **Easy Integration:** With a straightforward setup and intuitive interface, users can quickly run the project locally and experience the beauty of ASCII  videos in their **web browser**.

  ## Running the Program
1. **Download the Repository:**
* Download the project repository containing files like [sketch.js](https://github.com/Etutku/Formal_Languages_Projects/blob/main/ASCII%20Video/sketch.js), [style.css](https://github.com/Etutku/Formal_Languages_Projects/blob/main/ASCII%20Video/style.css), and [index.html](https://github.com/Etutku/Formal_Languages_Projects/blob/main/ASCII%20Video/index.html).
3. **Open in a Code Editor:**
* Use a [code editor](https://editor.p5js.org/etutkugayda/full/STZ9tNBj1) to open the project.
5. **Install a Local Server:**
* If needed, set up a local server. Use extensions like "Live Server" in Visual Studio Code.
7. **Run the Program:**
* Open sketch.html in your browser to start the program.
* Grant camera access when prompted.
9. **Interact and Customize:**
*Experiment with different character sets and parameters in real-time.

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

