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
    if intentName == "whatismathfun":
        return fun_math(intent, session)
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
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to prime learn! " \
                    "You can know interesting facts about maths by saying Tell me math fun"
    repromptText =  "You can know interesting facts about maths by saying Tell me math fun"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def fun_math(intent, session):
    import random
    index = random.randint(0,len(prime)-1)
    cardTitle = "Hello"
    sessionAttributes = {}
    speechOutput = "Prime learn that is actually a math fact is that " + prime[index] 
    repromptText = "You can know interesting facts about maths by saying Tell me math fun"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using prime learn Alexa Skills Kit. " \
                    "Have a great time! "
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



prime = [ "There is no largest prime number." ,
          "The sum of the interior angles of a triangle is 180 degrees" ,
          "There is a largest prime number in the integers modulo n",
          "The Fibonacci sequence is encoded in the number 1/89" ,
          "If you write out pi to two decimal places, backwards it spells pie." ,
          "A French word for pie chart is camembert." ,
          "The spiral shapes of sunflowers follow a Fibonacci sequence.",
          "A pizza that has radius z and height a has volume Pi times z square multiply by a." ,
          "The word hundred is derived from the word hundrath, which actually means 120 and not 100." ,
          "In a room of just 23 people there’s a 50% chance that two people have the same birthday." ,
          "Zero is the only number that can't be represented in Roman numerals.",
          "six multiply by 9 and then add six and nine to them is equal to sixty nine." ,
          "We tend to think of odd numbers as male and even numbers as female." ,
          "If you shuffle a pack of cards properly, chances are that exact order has never been seen before in the whole history of the universe." ,
          "Zero is an even number.",
          "There's not enough space in the known universe to write out a googolplex on paper.",
          "The most popular favourite number is 7.",
          "7 also shows up a lot in human culture.",
          "The number 4 is considered unlucky in much of Asia.",
          "Cicadas use prime numbers as an evolutionary strategy.",
          "10 factorial seconds is exactly 6 weeks." ,
          "Take any four digit number, follow these steps, and you'll end up with 6174." ,
          "555 is used by some in Thailand as slang for hahaha, because the word for five is pronounced ha." ,
          " after a million, billion and trillion , A quadrillion, quintillion, sextillion, septillion, octillion, nonillion, decillion and undecillion come" ,
          "Plus and Minus symbols were used as early as 1489 A.D" ,
          "2 and 5 are the only primes that end in 2 or 5" ,
          "An icosagon is a shape with 20 sides" ,
          "'FOUR' is the only number in the English language that is spelt with the same number of letters as the number itself" ,
          "Have you ever noticed that the opposite sides a die always add up to seven." ,
          "Trigonometry is the study of the relationship between the angles of triangles and their sides",
          "Abacus is considered the origin of the calculator" ,
          "A 'jiffy' is an actual unit of time for 1/100th of a second"
        ]
