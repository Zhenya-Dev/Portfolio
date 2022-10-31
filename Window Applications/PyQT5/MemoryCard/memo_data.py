from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

new_quest_templ = 'New question'
new_answer_templ = 'New answer'

text_wrong = 'Wrong'
text_correct = 'Right'


class Question():
    # stores information about one question
    def __init__(self, question=new_quest_templ, answer=new_answer_templ,
                 wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True
        self.attempts = 0
        self.correct = 0

    def got_right(self):
        # changes the statistics after getting the correct answer
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        # changes the statistic by getting the wrong answer
        self.attempts += 1


class QuestionView():
    # maps data and widgets to display a question
    def __init__(
            self,
            frm_model,
            question,
            answer,
            wrong_answer1,
            wrong_answer2,
            wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def change(self, frm_model):
        # updating data already associated with an interface
        self.frm_model = frm_model

    def show(self):
        # displays all the data from the object
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)


class QuestionEdit(QuestionView):
    # used if the form needs to be edited: sets event handlers that save the
    # text
    def save_question(self):
        # saves the text of the question
        # копируем данные из виджета в объект
        self.frm_model.question = self.question.text()

    def save_answer(self):
        # saves the text of the correct answer
        # копируем данные из виджета в объект
        self.frm_model.answer = self.answer.text()

    def save_wrong(self):
        # saves all wrong answers
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()

    def set_connects(self):
        # sets event handlers in widgets to save data
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong)
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)

    def __init__(
            self,
            frm_model,
            question,
            answer,
            wrong_answer1,
            wrong_answer2,
            wrong_answer3):
        super().__init__(
            frm_model,
            question,
            answer,
            wrong_answer1,
            wrong_answer2,
            wrong_answer3)
        self.set_connects()


class AnswerCheck(QuestionView):
    def __init__(
            self,
            frm_model,
            question,
            answer,
            wrong_answer1,
            wrong_answer2,
            wrong_answer3,
            showed_answer,
            result):
        super().__init__(
            frm_model,
            question,
            answer,
            wrong_answer1,
            wrong_answer2,
            wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        if self.answer.isChecked():
            # the answer is correct, write it down and reflect it in the
            # statistics
            self.result.setText(text_correct)
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_right()
        else:
            # the answer is wrong, write it down and reflect it in the
            # statistics
            self.result.setText(text_wrong)
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_wrong()


class QuestionListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []

    def rowCount(self, index):
        return len(self.form_list)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question

    def insertRows(self, parent=QModelIndex()):
        position = len(self.form_list)
        self.beginInsertRows(parent, position, position)
        self.form_list.append(Question())
        self.endInsertRows()
        QModelIndex()
        return True

    def removeRows(self, position, parent=QModelIndex()):
        self.beginRemoveRows(parent, position, position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]


def random_AnswerCheck(
        list_model,
        w_question,
        widgets_list,
        w_showed_answer,
        w_result):
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(
        frm,
        w_question,
        widgets_list[0],
        widgets_list[1],
        widgets_list[2],
        widgets_list[3],
        w_showed_answer,
        w_result)
    return frm_card
