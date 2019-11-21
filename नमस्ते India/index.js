// This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK (v2).
// Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
// session persistence, api calls, and more.
const Alexa = require('ask-sdk-core');

const LaunchRequestHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'LaunchRequest';
    },
    handle(handlerInput) {
        const speechText = 'नमस्ते, आपका स्वागत है नमस्ते India Alexa Skill में ,  आप इस Skill से jokes सुन सकते है और India के Facts भी सुन सकते है. '
                            + 'Jokes सुनाने के लिए बोलिये, एक Joke सुनाओ. '
                            + 'India के Facts सुनाने के लिए बोलिये,  एक Fact बताओ.  ';
        return handlerInput.responseBuilder
            .speak(speechText)
            .reprompt(speechText)
            .getResponse();
    }
};
const factIntentHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'IntentRequest'
            && handlerInput.requestEnvelope.request.intent.name === 'factIntent';
    },
    handle(handlerInput) {
        const factIndex = Math.floor(Math.random() * facts.length);
        const randomFact = facts[factIndex];
        const speechText = 'India के बारे में Fact ये है की , ' + randomFact;
        return handlerInput.responseBuilder
            //.speak(speechText  + '<audio src="soundbank://soundlibrary/human/amzn_sfx_crowd_applause_03"/>'  + ' दूसरा Fact सुनाने के लिए बोलिये एक Fact बताओ या Skill से बाहर आने के लिए बोलिये बंद करीये या Stop')
            .speak(speechText)
            //.reprompt('Jokes सुनाने के लिए बोलिये, एक Joke सुनाओ. India के Facts सुनाने के लिए बोलिये, एक Fact बताओ.  ')
            .getResponse();
    }
};

const jokeIntentHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'IntentRequest'
            && handlerInput.requestEnvelope.request.intent.name === 'jokeIntent';
    },
    handle(handlerInput) {
        const jokeIndex = Math.floor(Math.random() * jokes.length);
        const randomJoke = jokes[jokeIndex];
        const speechText = 'अब आप joke सुनिए , ' + randomJoke;
        return handlerInput.responseBuilder
            //.speak( speechText + '<audio src="soundbank://soundlibrary/human/amzn_sfx_crowd_applause_01"/> <audio src="soundbank://soundlibrary/human/amzn_sfx_laughter_giggle_01"/>' + ' Dusra joke Sunane Ke liye boliye Ek joke sunao ya Skill se bahar aane ke liye boliye Stop')
            .speak(speechText)
            //.reprompt('Jokes सुनाने के लिए बोलिये, एक Joke सुनाओ. India के Facts सुनाने के लिए बोलिये,  एक Fact बताओ. ')
            .getResponse();
    }
};

const HelpIntentHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'IntentRequest'
            && handlerInput.requestEnvelope.request.intent.name === 'AMAZON.HelpIntent';
    },
    handle(handlerInput) {
        const speechText =  'नमस्ते, आपका स्वागत है नमस्ते India Alexa Skill में ,  आप इस Skill से jokes सुन सकते है और India के Facts भी सुन सकते है. '
                            + 'Jokes सुनाने के लिए बोलिये, एक Joke सुनाओ. '
                            + 'India के Facts सुनाने के लिए बोलिये,  एक Fact बताओ.' ;
                            

        return handlerInput.responseBuilder
            .speak(speechText)
            .reprompt(speechText)
            .getResponse();
    }
};
const CancelAndStopIntentHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'IntentRequest'
            && (handlerInput.requestEnvelope.request.intent.name === 'AMAZON.CancelIntent'
                || handlerInput.requestEnvelope.request.intent.name === 'AMAZON.StopIntent');
    },
    handle(handlerInput) {
        const speechText = 'शुक्रिया नमस्ते India Alexa Skill उपयोग करने के लिए. कृपया दुबारा ज़रूर उपयोग करे , ';
        return handlerInput.responseBuilder
            .speak(speechText)
            .getResponse();
    }
};
const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse();
    }
};

// The intent reflector is used for interaction model testing and debugging.
// It will simply repeat the intent the user said. You can create custom handlers
// for your intents by defining them above, then also adding them to the request
// handler chain below.
const IntentReflectorHandler = {
    canHandle(handlerInput) {
        return handlerInput.requestEnvelope.request.type === 'IntentRequest';
    },
    handle(handlerInput) {
        const intentName = handlerInput.requestEnvelope.request.intent.name;
        const speechText = `You just triggered ${intentName}`;

        return handlerInput.responseBuilder
            .speak(speechText)
            //.reprompt('add a reprompt if you want to keep the session open for the user to respond')
            .getResponse();
    }
};

// Generic error handling to capture any syntax or routing errors. If you receive an error
// stating the request handler chain is not found, you have not implemented a handler for
// the intent being invoked or included it in the skill builder below.
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        console.log(`~~~~ Error handled: ${error.message}`);
        const speechText = `Sorry, I couldn't understand what you said. Please try again.`;

        return handlerInput.responseBuilder
            .speak(speechText)
            .reprompt(speechText)
            .getResponse();
    }
};


const jokes = [ 'English में. He is so talented,  हिंदी में. बहुत हरामी चीज है ये. ',
                'घर की इज़्ज़त बेटियों के हाथ में होती है और. Property के कागज नालायक के हाथ में होती है. ',
                'Amazon को लड़के नहीं पसंद इसलिए उसने अपने assistant का नाम Alexa रख दिया. ',
                'शादी सुदा आदमी जब कहे की वो सोच के बताएगा उसका मतलब है की वो अपनी बीवी से पूछ के बताएगा. ',
                'आज कल बच्चो से ज्यादा मच्छर responsible है, शाम से पहले घर आ जाते है. ',
                'खून में तेरे गर्मी, गर्मी में तेरा खून, ऊपर सूरज, निचे धरती, बिच में May and June, हे भगवान्. ',
                'आज Facebook ने बचा लिया, बीवी का birthday था और याद ही नहीं  था. ',
                'हम भी तेरी गलियों से गुज़रते थे, फिर तम्हारे पापा ने देख लिया. ',
                'तुमको देखा तो ये ख्याल आया, पता नहीं क्या खाके ये ख्याल आया. ',
        
];

const facts = [
        'Algebra , Trignometory और Differentiation का Invention India में हुआ है. ',
        'India में बंदरो की संख्या 5 करोड़ है. ',        
        'कमल के फूल को India के साथ वियतनाम के National Flower होने का भी गौरव प्राप्त है. ',
        'जैसलमेर के किले में शहर के 25% निवासी रहते है. ',
        'Chess का Invention भारत में हुआ था. ',
        'विश्व का नंबर ओने संविंधान भारत का है. ',
        'Pentium Chip का अविष्कार विनोद धाम ने किया था. ',
        'Hotmail का Development साबिर भाटिया ने किया था. ',
        'America में 38% भारतीय Doctors है. ',
        'नासा में 36% वैज्ञानिक भारतीय है. ',
        'भारत 90 देशो का software बेचता है. ',
        'शुन्य की खोज भारत में हुई थी. ',
        'चाय सबसे ज्यादा भारत में पि जाती है. ',
        'सबसे ज्यादा फिल्म भारत में बनती है. ',
        'भारत ने चाँद पर पानी की खोज सबसे पहले की है. ',
        'भारत में सबसे ज्यादा दूध है. '
];

// This handler acts as the entry point for your skill, routing all request and response
// payloads to the handlers above. Make sure any new handlers or interceptors you've
// defined are included below. The order matters - they're processed top to bottom.
exports.handler = Alexa.SkillBuilders.custom()
    .addRequestHandlers(
        LaunchRequestHandler,
        factIntentHandler,
        jokeIntentHandler,
        HelpIntentHandler,
        CancelAndStopIntentHandler,
        SessionEndedRequestHandler,
        IntentReflectorHandler) // make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
    .addErrorHandlers(
        ErrorHandler)
    .lambda();
