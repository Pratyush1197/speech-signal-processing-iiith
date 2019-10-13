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
| 2.           |To Translate any sentence from English to specific language and vice-versa Give input in the text-box in the specific language page | We get the translated text on button click | Data can be text value only| Translated Text is shown | Translated Text is shown  | Pass        | None     |

****

In case if it doesn’t work on some browsers, list down the browsers along with the versions here


| S. No | Browser           | Version  | Works(Yes/No) |
|-------|-------------------|----------|---------------|
| 1.    | Internet Explorer | 18, 17    | Yes           |
| 2.    | Chrome            | 77, 75, 74 | Yes           |
| 3.    | Firefox           | 66, 67, 68 | Yes           |
| 4.    | Opera             | 60, 58, 61 | Yes           |



 
The main objective of this experiment is to make the student understand and appreciate the difficulties in automating the task of speech signal-to-symbol transformation. The students are expected to understand terms such as phones, phonemes, syllables, transliteration, pitch or fundamental frequency, quasi-periodicity. The student should gain a good understanding of the speech signal by visual inspection. Given a speech waveform one should be able to discriminate between silence and speech, voiced speech and unvoiced speech. The student should be able to draw the speech waveform for a given word with appropriate time durations and relative amplitudes of the constituent phones.

Record speech signal of a sentence in any of the Indian languages, identify and mark by listening, manually, the boundaries of words and subword units (such as syllables and phonemes). Draw on a piece of paper the speech waveform for the first few words of the sentence with appropriate time durations and relative amplitudes of various sounds, clearly marking the various subword boundaries.

Step 1: Write down a sentence
-----------------
Write down a sentence in any Indian language, preferably your native language, on a piece of paper or your note book. Also, write down the sentence in English the way you would probably write it if you were writing a mail to your friend in your language

Eg: Let us consider a sentence in Hindi:

Utt #1: भारत हमार देश है

Transliteration in English: Bharat hamara desh hai

or in Telugu:

Utt #2: శ్రీ ఎమ్ వెన్కయ్య నాయ్దు  చెప్పెరు

Transliteration in English: ShrI M. Venkaiahnaidu chepperu

Step 2: Transliteration
-----------------
Transliteration is the process of writing one language using the script of another language. For example, the Hindi utterance considered in Step 1 is also written within brackets in English alphabets. The primary advantage of writing Hindi or any other Indian languages in English is that one can read it on a computer even if fonts for Devanagari (Hindi or Sanskrit script) or other Indian languages are not installed or rendered properly on our machine. Also, it is easier to write and debug programs using these English alphabets, till the time Indian language support for computers becomes widespread. In such a scenario, all softwares on our computer wiil be in our native script and one can write programs using our native script instead of English.

The transliteration of the Hindi utterance given in Step 1 (written using English alphabets or Latin script) uses a convention to write down Hindi alphabets in English. Eg. Bhaa is used for भा. Somebody else may write it as bhaa or BhA or bhA . The point here is that, there is a need for a common rule or convention, if followed by every one make life easier and avoids confusion during discussions or when programs are shared. ITRANS code is one such convention used to write Indian language alphabets in English.

Transliteration in English: Bharat hamara desh hai

ITRANS code: sri em ve.nkayyanayudu chepperu

Step 3: Record the speech signal
-----------------
Record a speech utterance using any sound recording utility at a sampling rate of 8 kHz or 16 kHz, at 16 bits per sample. Some of the recording utilities that can be used are the one provided as part ofthis virtual lab, or other third party utilities such as wavesurfer, audacity or praat, which can be freely downloaded from the net.

It is assumed that the sound card is configured properly on your machine and you are able to record and playback audio signals.

Step 4: Study the speech waveform
-----------------
Display the recorded speech signal using any waveform analysis utility.

Zoom in, select and listen to shorter segments of the speech waveform.

Try to identify regions of speech and nonspeech (silence) by visual inspection.

Step 5: Transcription using native script of the language
-----------------
Play the speech waveform.

By listening to the speech, write down on a piece of paper the utterance in the native script of the language.

Step 6: Transcription into English using ITRANS code tables
-----------------
Transcribe the utterance into English using ITRANS code tables.

ITRANS code: sri em ve.nkayyanayudu chepperu

ITRANS code is the common transliteration code for Indian languages. Using these ITRANS code tables, any Indian language script can be transcribed into English. For each of the Indian language a separate ITRANS code table is used to transcribe the script from the given language into English.

Step 7: Deriving the syllable-like units from English transcription
-----------------
Split the utterance (text in ITRANS code) into syllable-like units. That is the ITRANS code text representation of the utterance is divided into subword units such as syllable-like units (text to symbol transformation, i.e., sentence to subword units). Here syllable-like units are the symbols corresponds to the segments of the speech signal.
Reasons for choosing the syllable-like units as symbols against to phonemes (consonants or vowels (C or V)):

(1) It is very difficult to segment the speech data into phonemes.
(2) Due to coarticulation the effect of consonants is observed in the adjacent vowels.
(3) A character in an Indian language scripts is close to a syllable, and is typically one of the forms: V, CV, CCV, CVC, CCVC and CVCC, where C is a consonant and V is a vowel.

Utterance in ITRANS code: sri ve.nkayyanayudu chepperu

Syllable-like units of the utterance : sri em ve.n ka yya na yu du che ppe ru

Step 8: Identifying the boundaries of the syllable-like units in speech waveform
-----------------
Manually mark the boundaries of the syllable-like units by listening to the speech file segment by segment. The marked syllable boundaries and the associated waveform are shown in Figure 2. In the derived syllable boundaries some of the syllables present in the transcription are missing and some new syllables are marked. The expected syllable boundaries for a given speech file as per the transcription are shown in Figure 3.

Repeat the entire exercise with phoneme as the subword unit.











This is an electron Desktop app for processing the audio wave. With this application we can change the sampling frequency of any audio wave, listen the changes
and the graph can be plotted on the screen using matplotlib library of python. 

**Installation**
1. First clone the repository
2. run `npm install` inside the folder 
3. run `pip install -r requirements.txt` 
4. run `npm run start`

Your application will start on your local machine
