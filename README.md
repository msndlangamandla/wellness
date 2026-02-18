# wellness
I was explaining what AI is to my mother. In true mom fashion, she requested for me to make her a fitness agent. 

If like me, you are struggling wrapping your mind around what AI is and what it has got to do with you. This is a fun way to understand it in a way that make a lot of sense to me.
I am a data person, have been in the data space professionally for 14 years now. I like to get my hands dirty when trying to understand a concept. I had been searching far
and wide for a course or something to explain to me what AI is. Outside of AI hahah jokes. I did ask AI but what i was lacking was practicals. To actually work with LLM(s) 
myself until they made sense to me. If you are in the position I was in, where you were searching for something more tangible and beyond the think pieces of ethics of AI or
over simplified functional use cases. This is a good project to play around with. A lot of the code in here was learned from a brilliant man called Ed Donner, cant stress enough 
how brilliant the man is and how he technically got me as half excited as he is about AI. Dont know if any of us can really match his excitement :)
I made this project my own. if you have taken Ed's classes you will see how drastically different my project is but how it follows the same AI pattern of having one agent do work,
then having another agent validate the response. Which is such a neat trick for lessening hallucinations. 

Things you can improve on when making this yours
1. my responseModelFormat model -- I am interested in knowing if its possible to not have to spell out all the days of the week. if that could be automated somehow. I will probabaly explore this further. Just not at this moment, but if you figure this out, i would like to hear/see
2. this point is related to 1st one, but would be nice to sort of iterate over the days when calling save_plans instead of calling them out
3. fun things to also add that i will definitely add later -- using gradio (reason wasnt so keen this time around is for mom to use this fully i would have to host this vs my thought process of just sending her an email of her working plan each week from here)


Things That I put effort in that were not in Ed's course
1. adding a database aka file to save the weekly workout plan
2. also all the database functions to interact with said database
3. making the agent to start from a prompt requirement vs empowering it with a file of information to be an expert at saying something about someone. this will go over your head if you didnt take Ed's class but that is ok. really not important but worth mentioning for those to whom it will make sense to.
