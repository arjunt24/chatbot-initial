import parser
import cryptobot as cb

while True:
    # takes in input from command line
    query = input("> ")
    if query == "q":
        break;

    parsed_query = parser.parse(query)[0]
    cryptos = parser.parse(query)[1]

    response = cb.respond(parsed_query)

    function_call = "calling " + response[0] + " function on " + parser.unparse(response, cryptos)

    if parser.unparse(response, cryptos) == "off-topic":
        print("off topic")
    else:
        # print(input)
        print(parsed_query)
        print(cryptos)
        print(function_call)
