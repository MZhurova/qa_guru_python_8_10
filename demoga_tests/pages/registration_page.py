import os
from selene import have
from selene.support.shared import browser

import tests


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register_user(self, mariya):
        browser.element('#firstName').type(mariya.first_name)
        browser.element('#lastName').type(mariya.last_name)
        browser.element('#userEmail').type(mariya.email)
        browser.element('label[for="gender-radio-2"]').click()
        browser.element('#userNumber').type(mariya.fhone_nomber)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(mariya.date_of_birth.year)
        browser.element('.react-datepicker__month-select').type(mariya.date_of_birth.strftime('%B'))
        browser.element(f'.react-datepicker__day--00{mariya.date_of_birth.day}').click()
        browser.element('#subjectsInput').type(mariya.subjects).press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'image/{mariya.picture}')))
        browser.element('#currentAddress').type(mariya.address)
        browser.element('#react-select-3-input').type(mariya.state).press_enter()
        browser.element('#react-select-4-input').type(mariya.city).press_enter()
        browser.element("#submit").click()

    def assert_registred_date(self, mariya):
        full_name = f'{mariya.first_name} {mariya.last_name}'
        state_and_city = f'{mariya.state} {mariya.city}'
        date_of_birth = f'0{mariya.date_of_birth.day} {mariya.date_of_birth.strftime("%B")},{mariya.date_of_birth.year}'
        browser.element('.table').all('td').even.should(
            have.texts(
                full_name,
                mariya.email,
                mariya.gender,
                mariya.fhone_nomber,
                date_of_birth,
                mariya.subjects,
                mariya.hobbies,
                mariya.picture,
                mariya.address,
                state_and_city
            ))
        return self
