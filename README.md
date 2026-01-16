# MentorMindAI
## Smart Video Evaluation and Accessibility Engine

MentorMindAI is an AI-powered backend system that evaluates teaching quality from recorded videos and converts educational content into accessible learning formats.  
The platform uses ONNX-based machine learning models, FastAPI, and asynchronous processing to provide scalable, reproducible, and fair video evaluations.

---

## Table of Contents

- Problem Statement  
- Solution Overview  
- Key Features  
- Accessibility Modes  
- System Architecture  
- Project Structure  
- Technology Stack  
- Installation and Setup  
- Running the Application  
- API Endpoints  
- Screenshots  
- Contributors  
- Future Scope  
- License  

---

## Problem Statement

Teaching quality evaluation is often subjective and inconsistent. Additionally, standard video-based learning is not accessible to learners with visual, hearing, or cognitive challenges.

There is a need for:
- Objective teaching quality assessment  
- Automated feedback for mentors  
- Inclusive and accessible learning formats  

---

## Solution Overview

MentorMindAI provides:
- AI-based scoring of teaching videos  
- Deterministic and reproducible evaluation metrics  
- Automatic conversion of videos into accessible modes  

---

## Key Features

### AI Video Scoring System

Each uploaded teaching video is evaluated using ONNX models across the following dimensions:

- Clarity  
- Engagement  
- Pace  
- Filler Word Usage  
- Technical Depth  
- Weighted Overall Score  

Each metric is processed independently to ensure fairness and transparency.

---

## Accessibility Modes

### Blind Mode
Generates audio narration describing both visual and spoken content.

### Deaf Mode
Automatically generates subtitles using Whisper Speech-to-Text and exports `.srt` files.

### Easy Mode
Produces simplified narration using text summarization and text-to-speech for better comprehension.

---

## System Architecture

