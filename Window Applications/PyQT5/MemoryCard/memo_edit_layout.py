# Window for editing a question
from PyQt5.QtWidgets import QLineEdit, QFormLayout

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Question:', txt_Question)
layout_form.addRow('Correct answer:', txt_Answer)
layout_form.addRow('Wrong option №1:', txt_Wrong1)
layout_form.addRow('Wrong option №2', txt_Wrong2)
layout_form.addRow('Wrong option №3:', txt_Wrong3)

