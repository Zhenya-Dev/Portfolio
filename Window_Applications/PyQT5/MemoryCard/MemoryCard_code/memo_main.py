from PyQt5.QtCore import QTimer

from memo_app import *
from memo_data import *
from memo_main_layout import *
from memo_card_layout import *
from memo_edit_layout import txt_Question, txt_Answer
from memo_edit_layout import txt_Wrong1, txt_Wrong2, txt_Wrong3

main_width, main_height = 1000, 450
card_width, card_height = 600, 500
time_unit = 1000

questions_listmodel = QuestionListModel()
frm_edit = QuestionEdit(
    0,
    txt_Question,
    txt_Answer,
    txt_Wrong1,
    txt_Wrong2,
    txt_Wrong3)
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
frm_card = 0
timer = QTimer()
win_card = QWidget()
win_main = QWidget()


def testlist():

    frm = Question('Яблоко', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question('Дом', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Мышь', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)


def set_card():
    # sets how the card window looks like
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)


def sleep_card():
    # the card is hidden for the time specified in the timer
    win_card.hide()
    timer.setInterval(time_unit * box_Minutes.value())
    timer.start()


def show_card():
    # shows window (by timer), timer stops
    win_card.show()
    timer.stop()


def show_random():
    # show random question
    global frm_card
    frm_card = random_AnswerCheck(
        questions_listmodel,
        lb_Question,
        radio_list,
        lb_Correct,
        lb_Result)
    frm_card.show()
    show_question()


def click_OK():
    # checks the question or uploads a new question
    if btn_OK.text() != 'Next question':
        frm_card.check()
        show_result()
    else:
        # the label on the button is 'Next', so we create the next random
        # question:
        show_random()


def back_to_menu():
    # return from test to editor window
    win_card.hide()
    win_main.showNormal()


def set_main():
    # задаёт, как выглядит основное окно
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список вопросов')
    win_main.setLayout(layout_main)


def edit_question(index):
    # loads into the edit form the question and answers corresponding to the
    # passed string
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()


def add_form():
    # adds a new question and suggests changing it
    questions_listmodel.insertRows()
    last = questions_listmodel.rowCount(0) - 1
    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index)
    edit_question(index)

    txt_Question.setFocus(Qt.TabFocusReason)


def del_form():
    # delete question and switch focus
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())


def start_test():
    # at the beginning of the test, the form is associated with a random
    # question and shown
    show_random()
    win_card.show()
    win_main.showMinimized()

# Making the right connections:


def connects():
    list_questions.setModel(questions_listmodel)
    list_questions.clicked.connect(edit_question)
    btn_add.clicked.connect(add_form)
    btn_delete.clicked.connect(del_form)
    btn_start.clicked.connect(start_test)
    btn_OK.clicked.connect(click_OK)
    btn_Menu.clicked.connect(back_to_menu)
    timer.timeout.connect(show_card)
    btn_Sleep.clicked.connect(sleep_card)


# Program launch
testlist()
set_card()
set_main()
connects()
win_main.show()
app.exec_()
