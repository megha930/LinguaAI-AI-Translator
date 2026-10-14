# HORIZON TECHX

## ARTIFICIAL INTELLIGENCE INTERNSHIP PROJECT REPORT

### Project Title: LinguaAI – AI Language Translator

**Submitted by:** [Megha Kumari]
**Branch:** Computer Science and Engineering
**Internship Organization:** Horizon TechX
**Project Domain:** Artificial Intelligence
**Technology Stack:** Python, Streamlit, Requests, MyMemory Translation API

---

## 1. Abstract

LinguaAI is a web-based language translation application developed using Python and Streamlit. It allows users to enter text, select a source language and a target language, and request a translation through an online translation service.

The application provides a simple user interface, translation results, session-based translation history, and an option to download translated text. The project demonstrates the practical use of Python programming, web application development, API integration, and basic error handling.

## 2. Introduction

Language barriers can make communication difficult between people who speak different languages. LinguaAI aims to provide a simple interface for translating text between supported languages.

The project uses Streamlit to create the web interface and the MyMemory Translation API to request translations.

## 3. Objectives

- Develop a simple and user-friendly translation application.
- Allow users to select source and target languages.
- Integrate an external translation API.
- Display translation results clearly.
- Maintain translation history during the current application session.
- Allow users to download translated text.

## 4. Technologies Used

**Python:** Main programming language used for application logic.

**Streamlit:** Used to build the interactive web interface.

**Requests:** Used to send HTTP requests to the translation API.

**MyMemory Translation API:** Used to obtain translation results.

**Visual Studio Code:** Used to write and manage project files.

## 5. System Requirements

### Hardware

- Computer or laptop
- Internet connection

### Software

- Python
- Visual Studio Code
- Streamlit
- Requests library
- Modern web browser

## 6. System Workflow

1. The user opens the LinguaAI application.
2. The user selects the source language.
3. The user selects the target language.
4. The user enters the text to translate.
5. The application sends a request to the translation service.
6. The received result is displayed to the user.
7. Successful translations are added to the current session's history.
8. The user can download translated text.

## 7. Main Features

- Simple and responsive web interface
- Source and target language selection
- Online text translation
- Translation result display
- Session-based translation history
- Download translated text
- Clear history option
- Basic error handling

## 8. Testing

The following tests should be performed before submission:

| Test Case                         | Expected Result                                                    |
| --------------------------------- | ------------------------------------------------------------------ |
| Open the application              | Main interface appears                                             |
| Submit empty text                 | Warning is displayed                                               |
| Translate English text into Hindi | Hindi translation is displayed when the service responds correctly |
| View translation history          | Previous successful translations appear                            |
| Download a translation            | Text file is downloaded                                            |
| Disconnect from the internet      | Connection error is displayed                                      |

## 9. Limitations

- Translation requires an internet connection.
- Translation quality depends on the external translation service.
- The service may impose usage limits or become temporarily unavailable.
- Translation history is maintained only during the current session and is not permanently stored.

## 10. Future Enhancements

- Add permanent translation history using SQLite.
- Support additional languages.
- Improve translation validation and error reporting.
- Add user authentication.
- Deploy the application online.
- Improve accessibility and interface design.

## 11. Conclusion

LinguaAI demonstrates how Python, Streamlit, and an external API can be combined to build a simple language translation application. The project provides practical experience with user interface development, API integration, input validation, and error handling.

Further improvements can make the application more reliable, accessible, and suitable for broader use.

## 12. References

- Python: [https://www.python.org/](https://www.python.org/)
- Streamlit: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- Requests: [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
- MyMemory Translation API: [https://mymemory.translated.net/doc/spec.php](https://mymemory.translated.net/doc/spec.php)
