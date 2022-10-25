# the-big-boat
quiz patente nautica

## APP FLOW
- Launch app 
   1. load data
   2. create first page structure (1 page with 2 buttons)
- Quiz base
   1. create page SetupQuizBase
- Quiz vela
   1. create page SetupQuizVela
- Generate required quiz from template


OPEN POINTS
- create template (Class/Superclass) for SetupQuizPage
- create template (Class/Superclass) for QuizPage
- create template (Class/Superclass) for ResultPage

### TODO PER LORE

guardare il PEP8 dei warning che ti suggerisce come fare alcune modifiche:
- except senza richiamo all'eccezione
- variabili globali (non le conosco)
- metodi a cui passi il self ma non lo usano (@statichmethod)


Creare metodo che distrugge e lancia una nuova finestra


Classe LandingPage
Classe SetupQuiz 
- solo cose in comune 
Classe SetupQuizBase
Classe SetupQuizVela
Classe Quiz
Classe QuizRispMult
Classe QuizVF
Classe Risultati