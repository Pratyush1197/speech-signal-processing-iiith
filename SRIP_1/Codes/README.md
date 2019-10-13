Experiment Project Documentation
========================

Introduction
-----------------

This section captures the technical details related to the experiment development.

Project
-----------------

**Domain Name : **Computer Science & Engineering

**Lab Name : **Speech Signal processing** 

**Experiment Name : **Digital Signal Processing**

The objective of this lab is to provide hands on experience in processing speech signals for extraction of information for various applications.
Purpose of the project.In this we learned to process different audio samples,change their frequency andsamples/bits and listen to the processed speech to get a feel for effects of various signal processing operations on speech signals.


-----------------

The purpose of the project is to convert the **Digital Signal Processing** t  from **Java** to **Javascript**.

Project Developer Details

| S.NO | Name            | Year of study | Role          | E-mail Id                  | Github Handle                   |
|------|-----------------|---------------|---------------|----------------------------|---------------------------------|
| 1.   | Pratyush Narain | 3rd           | Web Developer | pratyushnarain97@gmail.com | https://github.com/Pratyush1197 |

Technologies and Libraries
-----------------

Technologies :
-----------------

1.  HTML
2.  CSS
3.  Javascript
4. Python
5. Electron.js

Libraries :   Pywave, Py-Matplotlib

Development Environment
-----------------

**OS :** LINUX

 Documents :
 -----------------

| S.NO | Link to Document   | Role                                                                          |
|------|--------------------|-------------------------------------------------------------------------------|
| 1.   | Procedure          | This document captures the instructions to run the  simulations               |
| 2.   | Test Cases         | This document captures the functional test cases of the experiment simulation |
| 3.   | Code Documentation | This document captures the  details related to code                           |

Process Followed to convert the experiment

1.  Understand the assigned experiment Java simulation
2.  Understanding the experiment concept
3.  Re-implement the same in javascript

Value Added by our Project
-----------------

1.  It would be beneficial for engineering students
2.  Highly beneficial for tier 2 and tier 3 college students who can use this to learn and understand the concept of perception learning.

Risks and Challenges
-----------------

Using a new desktop framework like Electron.js and integrating it with Pythont was a bit challenging as it is very less support on stackoverflow. One of the biggest challenge was to make small segments of audio. It was a great experience using Python library with javascript which helped to brush up my javascript and python concepts.

Experiment Procedure Documentation
========================

Introduction
-----------------

This document captures the instructions to run the simulation.

Instructions
-----------------

1.  To run the experiment Clone the repository given below

   https://github.com/Pratyush1197/speech-signal-processing-iiith.git

2.  Now open the folder speech-signal-processing-iiith
3.  Open SRIP folder
4. run `npm install` inside the folder 
5. run `pip install -r requirements.txt` 
6. run `npm run start`

Your application will start on your local machine

**Experiment Test Cases Documentation**
========================
Introduction
-----------------


This document captures the test cases of the experiment.

**Functional Test Cases**
-----------------



| Test Case Id | Test Scenario                                                    | Test Case                                     | Test Data                     | Expected Output                      | Actual Output                  | Test Result | Comments |
|--------------|------------------------------------------------------------------|-----------------------------------------------|-------------------------------|--------------------------------------|--------------------------------|-------------|----------|
| 1.           | To listen to a specific voice sample in specific language, Choose language name in Dropdown and Click on the play button. Frequency of audio sample can be also adjusted by selecting a certain frequency from dropdown | Click on the Play button under the voice sample or its subpart |  The audio is played with selected frequency|  |  The audio is played On button click audio with waveform is played  | |  The audio is played On button click audio with waveform is played  | Pass |       | None     |
| 2.           | change the bits/sample of any audio wave and the resultant waveform can be displayed on the graph. | We get the waveform generated on button click | Data can be text value only| Aliasing effect can also be added. | Audio wave is shown  | Pass        | None     |

****

In case if it doesn’t work on some browsers, list down the browsers along with the versions here


| S. No | Browser           | Version  | Works(Yes/No) |
|-------|-------------------|----------|---------------|
| 1.    | Internet Explorer | 18, 17    | Yes           |
| 2.    | Chrome            | 77, 75, 74 | Yes           |
| 3.    | Firefox           | 66, 67, 68 | Yes           |
| 4.    | Opera             | 60, 58, 61 | Yes           |



 
