questions=[ "Which country has the highest life expectancy? ",
"What is the most common surname in the United States? ...",
"Who was the Ancient Greek God of the Sun? ...",
"How many minutes are in a full week? ...",
"Aureolin is a shade of what color? ...",
"How many faces does a Dodecahedron have?"
]
answers=["Hong Kong","Smith","Apollo","Yellow","10080","12"]
count=0
for i in range(0,len(questions)):
    print(questions[i])
    a= input('give your answer')
    if a==answers[i]:
        count +=1
print (f"game over your score is {count}/6")        