def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])

def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "factIntent":
        return brain_teaser(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello! hello!"
    speechOutput =  "Hello , Welcome to Brain Teaser " \
                    "You can ask me brain teaser by saying Tell me brain teaser"
    repromptText =  "You can ask me brain teaser by saying Tell me brain teaser"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def brain_teaser(intent, session):
    import random
    index = random.randint(0,len(brainteaser)-1)
    cardTitle = "Hello"
    sessionAttributes = {}
    speechOutput = "brain teaser is that " + brainteaser[index] 
    shouldEndSession = False
    repromptText = "You can ask me brain teaser by saying Tell me brain teaser"
    shouldEndSession = False               
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using brain teaser Alexa Skills Kit. " \
                    "Have a great day! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



brainteaser = [ "A switch statement's case labels can occur inside if-else statements or in loops" ,
                "You can use #include in strange places." ,
                "Argument index specification in printf format specifier" ,
                "You can Ignore input in scanf" ,
                "you can Use range with switch cases" ,
                "Printf in C allows you to use variables for formatting format specifiers themselves" ,
                "a of index is same as index of a" ,
                "main() is not compulsory.",
                "C++ is an object oriented programming tool." ,
                "C++ is strongly typed language." ,
                "In 1979 Bjarne Stroustrup (Bell Labs), comes up with the C-With-Classes, and in 1983 with the C++." ,
                "American National Standards Institute (ANSI), has created an international standard for C++." ,
                "C++ is a superset of C.",
                "It is unnecessary to learn C first " ,
                "C++ is one of the predominant languages for the development of all kind of technical and commercial software." ,
                "C++ has bee used to develop other types of programming tools.",
                "Minimum requirement for a C++ program to run is a function." ,
                "C++ was build for Speed and portability." ,
                "C++ is a compiler type programming tool" ,
                "C++ is a NOT an interpreter"
                ]
