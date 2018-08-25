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
    if intentName == "global_warming":
        return global_warming(intent, session)
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
    speechOutput =  "Hello , Welcome to global warming facts! " \
                    "You can know about global warming by saying tell me about Global Warming"
    repromptText =  "You can know about global warming by saying tell me about Global Warming"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def global_warming(intent, session):
    import random
    index = random.randint(0,len(prime)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Global Warming:\n" + prime[index] 
    repromptText = "You can know interesting facts about global warming by saying tell me about about global warming"
    shouldEndSession = True                   
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using Global Warming Alexa Skills Kit. " \
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



prime = [ "Global warming, also referred to as climate change, is the observed century-scale rise in the average temperature of the Earth's climate system and its related effects.",
" Global warming occurs when carbon dioxide (CO2) and other air pollutants and greenhouse gases collect in the atmosphere and absorb sunlight and solar radiation that have bounced off the earth’s surface, trap the heat and cause the planet to get hotter. That's what's known as the greenhouse effect.",
"Global warming causes melting glaciers, early snowmelt, rising sea levels and severe droughts will cause more dramatic water shortages and increase the risk of wildfires.",
"Forests, farms, and cities will face troublesome new pests, heat waves, heavy downpours, and increased flooding. All those factors will damage or destroy agriculture and fisheries.",
"Because of global warming, allergies, asthma, and infectious disease outbreaks will become more common due to increased growth of pollen-producing ragweed, higher levels of air pollution, and the spread of conditions favorable to pathogens and mosquitoes.",
"In order to avoid the worst effects of climate change, we together with other countries, need to reduce our dependence on fossil fuels and start using clean energy instead.",
"To control Global Warming, you should power your home with renewable energy like solar or wind energy.",
"Saving water reduces carbon pollution, too. That's because it takes a lot of energy to pump, heat, and treat your water. So take shorter showers, turn off the tap while brushing your teeth, and switch to WaterSense-labeled fixtures and appliances.",
"Gas-smart cars, such as hybrids and fully electric vehicles, save fuel and money and hence help to control global warming.",
"Global Warming Cause: Methane emissions from animals, agriculture such as rice paddies, and from Arctic seabeds.",
"Global Warming Cause: Deforestation, especially tropical forests for wood, pulp, and farmland.",
"Global Warming has lead to Widespread extinction of species.",
"To save resources, you shouldn't use more energy than you need.",
"When you buy new energy-efficient appliances and electronics, it's important to dispose of the old ones in a planet-friendly way to save energy."
        ]
