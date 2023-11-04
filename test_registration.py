from selene.support.shared import browser
import os
from selene import have


def test_registration():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Mariya')
    browser.element('#lastName').type('Zhurova')
    browser.element('#userEmail').type('mzhurova4@mail.ru')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('9234324557')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="9"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1990"]').click()
    browser.element('[aria-label="Choose Thursday, October 4th, 1990"]').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../qa_guru_python_8_10/image/2012091208303549.png'))
    browser.element('#currentAddress').type('Tomsk, Altayskaya')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element("#submit").click()

    browser.element('.table-responsive').all('td:nth-child(2)').should(
        have.texts('Mariya Zhurova', 'mzhurova4@mail.ru', 'Female', '9234324557', '04 October,1990', 'Maths', 'Sports',
                   '2012091208303549.png', 'Tomsk, Altayskaya', 'Haryana Panipat'))
