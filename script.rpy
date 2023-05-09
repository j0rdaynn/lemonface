define j = Character("Jasmine", color="#FA19B7")
define h = Character("Huey", color="#FB7D23")
define g = Character("Grandad", color="#0059ff")
define r = Character("Riley", color="#d60000")
define t = Character("Tom", color="#4800ad")
default question_tally = 0

label start:
    scene blackk
    with fade
    show regular_huey
    h "People soak up anything they see without even giving it a second thought."

    h "Even though it may not seem like a big deal, social media misinformation
    can cause absolute chaos. From radicalized groups committing horriffic acts to having
    people change their perception of themselves."

    h "Which brings me into the first person i'm going to show you, Jasmine."

    hide regular_huey
    scene livingroom
    show resized_jas

    h "She's the eptiome of someone who looks like they'd believe just about anything."

    hide resized_jas
    show jas_w_phone

    h "She spends all of her morning, afternoons, and nights scrolling on tiktok"

    h "It's become quite an obsession for her."

    h "Because of how much she's on it, the app has tended to her algorithm."

    h "It knows what she likes, dislikes, saves, searches, everything under the sun."

    show regular_huey at left with moveinleft

    h "She started getting women on her for you page that are extremly beautiful"

    h "She started getting them so much that she now wants to become them.."

    h "Alot of the women on there potray themselves their looks to be genetics"

    h "While that is the case sometimes, it wasnt the case for this one."

    hide regular huey with moveinleft
    hide jas_w_phone
    scene blackbg
    show resize_phone with fade

    menu:
        "scroll to comments":
            hide resize_phone
            show commentss
    j "She puts lemon on her face for clear skin.."

    j "And she puts hot tea on her lips.."

    j "This must work if it worked her."

    j "If she can do that then I can too!"

    hide comments
    show phonecall

    t "Hey Honey, what's up?"

    j "Nothing much daddy! I wanted to know if you can buy me some
    lemons from teht store befor eyou come home?"

    t "Sure honey! But why would you need lemons?"

    menu:
        "To make lemonade":
            t "Okay that sounds fun! I'll bring home some tea and sugar too."

        "Mom needs them":
            t "Okay i'll add them on the list. Tell mommmy I said hi and I miss her!"

    j "thank you so much daddy!"

    t "No problem, i'll see you when i get home! See you later aligator"

    j "In a while crocodile!"

    hide phonecall
    scene bathroombg
    show beforelemon

    j "okay now time for the lemon!"

    hide beforelemon
    show lemon1 with fade
    show lemon2 with fade
    show lemon3 with fade
    show lemon4

    hide lemon1
    hide lemon2
    hide lemon3
    hide lemon4
    show facemasks

    j "Now to wait until the timer goes off."

    hide facemasks with dissolve
    scene phon2

    scene bathroombg

    j "Time for the big reveal!!"

    show blemish_jas

    j "OH MY GOSH MY FACE!!"
    j "It's ruined..."
    j "I need to ask what to do! I know just where to go."

    hide blemish_jas
    scene thehood with fade

    "Jasmine's making her way to the 'Freeman' Household."

    scene closedoor
    show riley_reg

    r "Man what you want.. i'm trying watch Thugnificant."

    r "... HUEY THERE'S A MONSTER AT THE DOOR!"

    j "Riley it's just me.."

    r "Jasmine?? You got possesed or something?"

    j "No !! I put lemon on my face and now my face is ruined."

    r "Yeah clearly. Who told you to put lemon on your face?"

    j "I was trying to get clear skin like a pretty girl on tiktok.
    She said that's how she got hers."

    r "And you fell for it like a sucka. Now she got you looking like a
    seasons pizza ad."

    j "RILEY!!"

    r "Alright monsters inc let me get Grandad, maybe he'd know how to fix your ugly.."

    hide riley_reg
    show grandad

    g "Dang Riley yelling my name through the whole neighborhood."

    g "Jasmine what'chu want? You got a little red sauce on your face."

    j "No Mr.Freeman, I put a lemon on my face and I need advice. Riley sai dyou'd know what to do?"

    g "So let me get this straight, you got a chemical burn from putting lemon across your face?"

    j "I think so."

    g "And how in the world did you end up getting that?"

    menu:
        "Tell him a tiktoker said she made her skin clear by doing so.":
            g "Well that's on you, why didn't you check first that nothing bad would happen if you did it?"

        "Tell him you did it for science experiment":
            g "What type of science experiement is that? Can't even fact check what it'd do their students.."

    j "I know.. I should've done my research. Well what am I going to do now??"

    g "Come inside and was that face off and we'll call Tom to get you some ointment."

    hide grandad with dissolve
    scene blackk
    show regular_huey

    h "They ended up calling her father, who then deicded to add child restrictions on her phone."

    h "He even took it up with Tiktok and emailled them to put a child viewing mode."

    h "Which eventually they did so stuff like this doesn't happen.."

    h "As for Goddess_25 or whatever her name is."

    h "They turned her comments off."

    h "Even though everything came to a good end I think we all learned a lesson."

    h "Stop beleiving everything you see on the internet."

    h "Please.."

    return
