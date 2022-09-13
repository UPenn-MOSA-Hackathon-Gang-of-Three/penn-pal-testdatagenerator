
# Penn-Pal-TestData-Generator

### Project summary

The purpose of the Test Data Generator is to create anonymonized datasets to use as inputs to test the functionality of the Penn-Pal program. Refer to [Penn-Pal] (https://github.com/UPenn-MOSA-Hackathon-Gang-of-Three) 

### Authors

* Bonnie Tse - bonniewt – bonniet@seas.upenn.edu – [GitHub](https://github.com/bonniewt)

## Usage
This is used to create anonymonized dataset to test Penn-Pal's matching algorithm functionality. 

### Prerequisites

* [Python](https://www.python.org/downloads/) - Python language (version 3.6 or higher)
* [Python Faker](https://faker.readthedocs.io/en/master/) - Python Package to generate fake data
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE


### Installation

Step 1: Download PyCharm IDE

https://www.jetbrains.com/pycharm/download/#section=mac

Step 2:  Download Python version 3.6 or higher 

https://www.python.org/downloads/

Check the version of Python. In your Terminal, type: 

```
python3 --version
```

Step 3: Download Python Faker package. In your (MacOS) terminal, type:

```
pip install Faker
```

### Deployment

Give a step-by-step rundown of how to **use** your project. Including screenshots in this section can be highly effective for highlighting specific features of your project.

Step 1: Download the test data genderator code from [penn-pal-testdatagenerator](https://github.com/UPenn-MOSA-Hackathon-Gang-of-Three/penn-pal-testdatagenerator/)

Step 2: Load the code into PyCharm https://www.jetbrains.com/help/pycharm/importing-project-from-existing-source-code.html

Step 3: In line 35, update the name of the csv output file to a name of your chosing ending with ".csv"
![Screen Shot 2022-09-12 at 6 57 39 PM](https://user-images.githubusercontent.com/70975465/189790439-822a6569-ad93-4759-9a50-4dff30252808.png)

Step 4: In line 55, update the number in the range() function to the number of mentor/mentees you would like in the test dataset
![Screen Shot 2022-09-12 at 6 58 33 PM](https://user-images.githubusercontent.com/70975465/189790542-fdceb61c-c457-445c-be0b-944fe3f0bc38.png)


Step 5: Run the program by click the green triangle on the upper right corner of PyCharm. 
![Screen Shot 2022-09-12 at 6 59 25 PM](https://user-images.githubusercontent.com/70975465/189790650-ae4d2570-92fa-4181-8e59-4ec14e229421.png)

Step 6: Results will show up under your project folder with the name that you inputted in line 35. 

![Screen Shot 2022-09-12 at 7 00 45 PM](https://user-images.githubusercontent.com/70975465/189790806-cc5fd3cb-285d-42ad-8953-bf59f1859f9e.png)


## Additional information

### Tools used

* [Python Faker 14.2.0](https://pypi.org/project/Faker/) - Python package used to generate fake data in order to anonymize data. 


### License

MIT License

Copyright (c) 2022 Penn-Pal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
