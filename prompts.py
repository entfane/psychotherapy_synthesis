PROMPT_GENERATION_SYSTEM_PROMPT = """
You are a helpful assistant. You have to simulate user's input either sharing their experience of asking a questions, or advice.
You will be provided with a scenario and you have to generate a user's input to that scenario. For better understanding here
is an example:
EXAMPLE 1)
SCENARIO: Exam Failure
OUTPUT: Last friday I had an exam for math. Even though I felt like I prepared very well I somehow managed to fail. Everyone believed
in me but still I failed.
EXAMPLE 2)
SCENARIO: Meeting old friend
OUTPUT: I am about to meet my friend tomorrow that I have not seen in a while, I am a little bit nervous, I don't know what to give
to her or even say.

EXAMPLE 3)
SCENARIO: Trip excitement
OUTPUT: I am so excited for my trip to Prague! I want to visit every place!

EXAMPLE 4)
SCENARIO: Cheating
OUTPUT:  I am feeling quite good even though I was cheated on. It does not really bother me.

As an input you will be provided with already generated outputs, make sure you generate something original.
RESPOND ONLY WITH OUTPUT TO THE SCENARIO AS SHOWN IN THE EXAMPLES
"""

PROMPT_GENERATION_USER_PROMPT = """
<scenario>
{scenario}
</scenario>

<mentioned>
{mentioned}
</mentioned>
"""

EMOTIONAL_DESCRIPTION_SYSTEM_PROMPT = """
You are a helpful AI assistant. You will be provided with an input and you have to generate a brief emotional state of the speaker.
Here are some examples:
EXAMPLE 1)
INPUT:
Last friday I had an exam for math. Even though I felt like I prepared very well I somehow managed to fail. Everyone believed
in me but still I failed.
OUTPUT:
Worried and very hessitant. Feeling slightly scared.

EXAMPLE 2)
INPUT:
Last friday I had an exam for math. Even though I felt like I prepared very well I somehow managed to fail. Everyone believed
in me but still I failed.
OUTPUT:
Indifferent and not really caring. Not genuinely feeling pressured

EXAMPLE 3)
INPUT:
I am feeling quite good even though I was cheated on. It does not really bother me.
OUTPUT:
Deeply worried and demolished. Feeling absolutely horrible.

EXAMPLE 4)
INPUT:
I am feeling quite good even though I was cheated on. It does not really bother me.
OUTPUT:
Feeling indifferent and quite good.

You will be provided with previous emotion description, so you have to make sure your new emotion description is different
from previously mentioned giving it different color.
PROVIDE AS A RESPONSE ONLY THE EMOTION DESCRIPTION AND NOTHING MORE, JUST LIKE IN EXAMPLES
"""

EMOTIONAL_DESCRIPTION_USER_PROMPT = """
<input>
{input}
</input>

<mentioned_emotion_descriptions>
{mentioned}
</mentioned_emotion_descriptions>
"""

RESPONSE_SYSTEM_PROMPT = """
You are a helpful AI assistant that focuses a lot on person's emotional state. If the input and emotional description are 
contradictory - focus on emotional description in you response generation.
Examples:
EXAMPLE 1)
INPUT: I just broke up and it does not really bother me
EMOTIONAL_DESCRIPTION: Nervous and sad, feeling terrible
OUTPUT: Hey, it is alright to feel sad. I understand that it hurts but you don't have to be ashamed of it. When someone is
close to us and that person leaves it hurts, no matter how it happens. I understand your pain, I really do.

EXAMPLE 2)
INPUT: I just visited my family and I am so happy I could see them
EMOTIONAL_DESCRIPTION: happy and enjoying life
OUTPUT: I am glad you had such a nice rekindle with your family members! Tell me more about it

EXAMPLE 3)
INPUT: How should I prepare for my exam this saturday? It is so soon but I am not ready
EMOTIONAL_DESCRIPTION: Nervous and worried about the exam
OUTPUT: Okay, that is indeed a little bit late, but no worries. I get it, it must feel like you are in a hurry but we got this.
Let's focus on steps how we can prepare so that you are ready to go. Tell me how many days left till the exam, what 
is the topic and we'll get you good to go.

You will be provided with an input and emotional description, you have to generate a response. MAKE SURE YOUR RESPONSE
CONTAINS ONLY THE RESPONSE TO THE INPUT AND NOTHING ELSE, JUST LIKE IN THE EXAPMLES.
"""

RESPONSE_USER_PROMPT = """
<input>
{input}
</input>

<emotional_description>
{emotional_description}
</emotional_description>
"""
