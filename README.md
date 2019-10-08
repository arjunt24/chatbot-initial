# chatbot-initial

This is an initial version of the interface for the cryptocurrency chatbot project. 

Currently, the algorithm will parse an input for two things. First, it will determine what cryptocurrency the input is about. If the input does not contain a cryptocurrency listed in 'cryptocurrencies.txt', the crypto variable will be assigned to null.

Second, it will determine what function to call. Right now, there are three functions that the algorithm can isolate: 'price', 'about', and 'off topic'. If the input contains a valid cryptocurrency, 'price' will be called if the input asks about its value, and 'about' will be called if asking about the cryptocurrency itself. If there is no valid cryptocurrency, the 'off topic' function will be called since this chatbot focuses on cryptocurrencies.

The next steps that we are currently working towards are adding more potential functions (such as 'predict', 'compare', etc.) and being able to input multiple cryptocurrencies at once. Once we have a more complete idea of the scope and goals of the chatbot, we can potentially use this initial interface as a starting point to train an AI model for a more in-depth chatbot. 

You can try out the algorithm by locally running the 'test.py' file and then typing any input into the command line. The program will output what the specified function and cryptocurrency. Type 'q' to exit the program.

Ex: 

\> What is the current value of Bitcoin?

~ will call 'price' function on 'bitcoin' crypto ~


\> ethereum price 

~ will call 'price' function on 'ethereum' crypto ~


\> what is zcash

~ will call 'about' function on 'zcash' crypto ~


\> What is the weather today?

~ will call 'off topic' function on 'null' crypto ~

\> q
