# Low vision reader project thing name tbd

This repository contains python and arduino code written for the 2026 UofT UTEK project.

The objective was to design a wearable low vision reader that captures symbols and text through a camera, processes it with Optical Character Recognition (OCR) and delivers it as speech output.

## Primary Features
- Connection to an HTTP server hosting the ESP32 camera feed using WiFi
- HTTP GET requests from a python script to process the camera feed to text using pytesseract (OCR)
- Using Pytts to convert text to audio

## Secondary Features
- Gesture control using Google's Hand Landmark Detection from Google Mediapipe Solutions
  - Storage & Replay
  - TTS activation/deactivation
  - Termination
- Distance Adaptability
- PDF Report of text scanned during each usage instance

## Future Additions
- [ ] Multilanguage support
- [ ] More dynamic
- [ ] Volume control
- [ ] Read sign language of the user??
- [ ] Reports/Analysis of text read and things seen that day
- [ ] Object detection/classification
- [ ] Add Links to APIs/models/additional libraries used
