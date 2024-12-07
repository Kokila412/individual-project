quiz=[
    {
        "q":"1.What is the fastest bird in the world?",
        "o":["A.Ostrich","B.Peregrine Falcon","C.Eagle","D.Spix's Macaw"],
        "a":"B"
    },
     {
        "q":"2.In 1768, Captain James Cook set out to explore which ocean?",
        "o":["A.Pacific Ocean","B.Atlantic ocean","C.Indian ocean","D.Arctic ocean"],
        "a":"A"
    },
     {
        "q":"3.Which did Viking people use as money?",
        "o":["A.Rune stones","B.Jewellery","C.Seal skins","D.Wool"],
        "a":"B"
    },
     {
        "q":"4.What is the main component of the sun?",
        "o":["A.Liquid lava","B.Molten iron","C.Rock","D.Gas"],
        "a":"D"
    }
]
def myQuiz(quiz):
    score=0
    for dict in quiz:
        print(dict["q"],"\n")
        for j in dict["o"]:
            print(j)
        print("\n")
        ans=input("print your answer").upper()
        if ans==dict["a"]:
            print("cool!!!!")
            score+=1
        else:
            print("looser!!!!")
    print(f"your score is {score} out of {len(quiz)} questions")
myQuiz(quiz)
