
easy_text = """A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose."""

medium_text = """A __1__ is created with the def keyword.  You specify the inputs a
function takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, number, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions."""

hard_text = """When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==)."""

easy_fill_in_the_blanks = ["__1__", "__2__", "__3__", "__4__"]
medium_fill_in_the_blanks = ["__1__", "__2__", "__3__", "__4__"]
hard_fill_in_the_blanks  = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__", "__9__", "__10__"]

easy_answers = ["world", "Python", "print", "HTML"]
medium_answers = ["function", "arguments", "None", "list"]
hard_answers = ["class", "method", "__init__", "instance", "__repr__", "__lt__", "__gt__", "__add__", "__sub__", "__eq__"]


level_mapping = {
    "easy": {"para": easy_text, "blanks": easy_fill_in_the_blanks, "answers": easy_answers},
    "medium": {"para": medium_text, "blanks": medium_fill_in_the_blanks, "answers": medium_answers},
    "hard": {"para": hard_text, "blanks": hard_fill_in_the_blanks, "answers": hard_answers}
}
# Ask a user to select difficulty, easy, medium hard
def ask_question():
    #ask_question function returns user selection of level in the game.
    #inputs: given choices
    #outputs: user selection of game level.
    difficulty = None
    while difficulty not in level_mapping.keys():
        print "Please select a game difficulty by typing it in!"
        print "Possible choices include easy, medium, and hard."
        difficulty = raw_input().lower().strip()
        if difficulty in level_mapping.keys():
            print "You've chosen " + difficulty + "!"
            print
        else:
            print "That's not an option!"
    return difficulty

def get_level_details(diff_level):
    #get_level_details returns the user_inputs of the game choices and brings out for user.
    return level_mapping.get(diff_level)

# #printing the questions and getting the answers from the user.
# def ask_for_answer(new_para, diff_level, index):
#     #ask_for_answer shows the paragraph and ask the user to fill in the blanks.
#
#     return
def update_tries(tries):
    #updated_tries returns the tries of the user to answer the blanks.
    #review the answer and checks if it is correct or not.
    tries = tries - 1
    if tries > 1:
        print "That isn't the correct answer!  Let's try again;  You have " + str(tries) + " tries left!"
    if tries == 1:
        print "That isn't the correct answer!  You only have 1 try left!  Make it count!"
    print
    return tries
#checking the user answers, and declaring if they win or loose.
def quiz_player(new_para, quiz_ans, tries, diff_lev, blanks):
    #quiz_player returns the winner or looser of the the game.
    # checks the answers and tells them if they won or lost.
    index = 0
    for token in quiz_ans:
        while tries > 0 and index < len(quiz_ans):
            print "The current paragraph reads as such:\n"
            print new_para
            user_input = raw_input("\nWhat should be substituted in for  " + blanks[index] + " ? ")
            if user_input.lower() != quiz_ans[index].lower():
                tries = update_tries(tries)
            else:
                print "\nCorrect!\n"
                new_para = new_para.replace(blanks[index], quiz_ans[index])
                index += 1
    if tries == 0:
        print "You've failed too many straight guesses!  Game over!"
    else:
        print new_para
        print "You Won!"

#Main game runner
def play_game():
    difficulty_level = ask_question()
    max_guesses = 5
    print "You will get 5 guesses per problem \n"
    level_details = get_level_details(difficulty_level)
    quiz_paragraph, quiz_fill_in_the_blanks, quiz_answers = level_details['para'], level_details['blanks'], level_details['answers']
    quiz_player(quiz_paragraph, quiz_answers, max_guesses, difficulty_level, quiz_fill_in_the_blanks)


play_game()
