from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from constants import globalConstants
from pathlib import Path
from datetime import date


class Test_NopCommerce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.url)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    
    def teardown_method(self):
        self.driver.quit()
    

    @pytest.mark.parametrize("username,password",[("adminuser@yourstore.com","123456789")])
    def test_invalid_login(self,username,password):

        self.waitForElementVisible((By.XPATH,globalConstants.invalidloginXpath))
        login = self.driver.find_element(By.XPATH,globalConstants.invalidloginXpath)
        login.click()

        self.waitForElementVisible((By.ID,globalConstants.emailID))
        emailInput = self.driver.find_element(By.ID,globalConstants.emailID)
        emailInput.send_keys(username)

        passwordInput = self.driver.find_element(By.ID,globalConstants.passwordID)
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.XPATH,globalConstants.loginXpath)
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,globalConstants.erroreMessageXpath)
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == globalConstants.erroreMessageText
        


    def test_valid_login(self):

        self.waitForElementVisible((By.XPATH,globalConstants.registerXpath))
        register = self.driver.find_element(By.XPATH,globalConstants.registerXpath)
        register.click()

        self.waitForElementVisible((By.ID,globalConstants.gender_male_ID))
        gender = self.driver.find_element(By.ID,globalConstants.gender_male_ID)
        gender.click()

        firstName = self.driver.find_element(By.ID,globalConstants.first_name_ID)
        firstName.send_keys("admin")

        lastName = self.driver.find_element(By.ID,globalConstants.last_name_ID)
        lastName.send_keys("user")

        self.waitForElementVisible((By.XPATH,globalConstants.dateOfBirthDayXpath))
        dateOfBirthDay = self.driver.find_element(By.XPATH,globalConstants.dateOfBirthDayXpath)
        dateOfBirthDay.click()

        dateOfBirthMonth = self.driver.find_element(By.XPATH,globalConstants.dateOfBirthMonthXpath)
        dateOfBirthMonth.click()

        dateOfBirthYear = self.driver.find_element(By.XPATH,globalConstants.dateOfBirthYearXpath)
        dateOfBirthYear.click()

        self.waitForElementVisible((By.ID,globalConstants.emailID))
        emailInput = self.driver.find_element(By.ID,globalConstants.emailID)
        emailInput.send_keys(globalConstants.emailInput)

        company = self.driver.find_element(By.ID,globalConstants.companyID)
        company.send_keys("HALIT HOLDING")

        passwordInput = self.driver.find_element(By.ID,globalConstants.passwordID)
        passwordInput.send_keys(globalConstants.passwordInput)

        confirmPassword = self.driver.find_element(By.ID,globalConstants.confirmPasswordID)
        confirmPassword.send_keys(globalConstants.passwordInput)

        registerBtn = self.driver.find_element(By.ID,globalConstants.registerBtnID)
        registerBtn.click()

        self.waitForElementVisible((By.XPATH,globalConstants.continueBtnXpath))
        continueBtn = self.driver.find_element(By.XPATH,globalConstants.continueBtnXpath)
        continueBtn.click()

        self.waitForElementVisible((By.XPATH,globalConstants.categoriesCumpoterXpath))
        categoriesCumpoter = self.driver.find_element(By.XPATH,globalConstants.categoriesCumpoterXpath)
        categoriesCumpoter.click()

        self.waitForElementVisible((By.XPATH,globalConstants.productNotebookXpath))
        notebook = self.driver.find_element(By.XPATH,globalConstants.productNotebookXpath)
        notebook.click()

        self.waitForElementVisible((By.XPATH,globalConstants.examineNotebookXpath))
        examinetNotebook = self.driver.find_element(By.XPATH,globalConstants.examineNotebookXpath)
        examinetNotebook.click()
        
        addToCartMacBook = self.driver.find_element(By.ID,globalConstants.addToCartMacBookID)
        addToCartMacBook.click()

        self.waitForElementVisible((By.XPATH,globalConstants.categoriesCumpoterXpath))
        categoriesElectronics = self.driver.find_element(By.XPATH,globalConstants.categoriesElectronicsXpath)
        categoriesElectronics.click()

        self.waitForElementVisible((By.XPATH,globalConstants.productCellPhoneXpath))
        cellPhone = self.driver.find_element(By.XPATH,globalConstants.productCellPhoneXpath)
        cellPhone.click()

        self.waitForElementVisible((By.XPATH,globalConstants.examineCellPhoneXpath))
        examineCellPhone = self.driver.find_element(By.XPATH,globalConstants.examineCellPhoneXpath)
        examineCellPhone.click()

        addToCartM8Android = self.driver.find_element(By.ID,globalConstants.addToCartM8Android)
        addToCartM8Android.click()

        self.waitForElementVisible((By.XPATH,globalConstants.goToCartXpath))
        goToCart = self.driver.find_element(By.XPATH,globalConstants.goToCartXpath)    
        goToCart.click()

        termOfService = self.driver.find_element(By.ID,globalConstants.termOfServiceID)
        termOfService.click()

        checkout = self.driver.find_element(By.ID,globalConstants.chechoutID)
        checkout.click()

        self.waitForElementVisible((By.ID,globalConstants.emailID))
        returningEmailInput = self.driver.find_element(By.ID,globalConstants.emailID)
        returningEmailInput.send_keys(globalConstants.emailInput)

        returningPasswordInput = self.driver.find_element(By.ID,globalConstants.passwordID)
        returningPasswordInput.send_keys(globalConstants.passwordInput)

        login = self.driver.find_element(By.XPATH,globalConstants.loginXpath)
        login.click()
        
        termOfService_2 = self.driver.find_element(By.ID,globalConstants.termOfServiceID)
        termOfService_2.click()

        checkout_2 = self.driver.find_element(By.ID,globalConstants.chechoutID)
        checkout_2.click()

        
        self.waitForElementVisible((By.ID,globalConstants.countryID))
        country = self.driver.find_element(By.XPATH,globalConstants.turkeyXpath)
        country.click()

        city = self.driver.find_element(By.ID,globalConstants.cityID)
        city.send_keys("Istanbul")

        adres_1 = self.driver.find_element(By.ID,globalConstants.adres_1_ID)
        adres_1.send_keys("Istanbul")

        adres_2 = self.driver.find_element(By.ID,globalConstants.adres_2_ID)
        adres_2.send_keys("Istanbul")

        postalCode = self.driver.find_element(By.ID,globalConstants.postalCodeID)
        postalCode.send_keys("34000")

        phoneNumber = self.driver.find_element(By.ID,globalConstants.phoneNumberID)
        phoneNumber.send_keys("01234567891")

        continueBtnAdress = self.driver.find_element(By.NAME,globalConstants.continueBtnName)
        continueBtnAdress.click()

        self.waitForElementVisible((By.ID,globalConstants.nextDayAirID))
        nextDayAir = self.driver.find_element(By.ID,globalConstants.nextDayAirID)
        nextDayAir.click()

        shippingContinueBtn = self.driver.find_element(By.XPATH,globalConstants.shippingContinueBtnXpath)
        shippingContinueBtn.click()

        self.waitForElementVisible((By.XPATH,globalConstants.creditCardXpath))
        creditCard = self.driver.find_element(By.XPATH,globalConstants.creditCardXpath)
        creditCard.click()

        nextStepContinueBtnPayment = self.driver.find_element(By.XPATH,globalConstants.nextStepContinueBtnPaymentXpath)
        nextStepContinueBtnPayment.click()

        self.waitForElementVisible((By.ID,globalConstants.cardHolderNameID))
        cardHolderName = self.driver.find_element(By.ID,globalConstants.cardHolderNameID)
        cardHolderName.send_keys("Akbank")

        cardNumber = self.driver.find_element(By.ID,globalConstants.cardNumberID)
        cardNumber.send_keys("4355084355084358")

        expirationDateDay = self.driver.find_element(By.XPATH,globalConstants.expirationDateDayXpath)
        expirationDateDay.click()

        expirationDateYear = self.driver.find_element(By.XPATH,globalConstants.expirationDateYearXpath)
        expirationDateYear.click()

        cardCode = self.driver.find_element(By.ID,globalConstants.cardCodeID)
        cardCode.send_keys("000")

        continueBtnPayment_2 = self.driver.find_element(By.XPATH,globalConstants.continueBtnPayment_2Xpath)
        continueBtnPayment_2.click()

        self.waitForElementVisible((By.XPATH,globalConstants.confirmXpath))
        confirm = self.driver.find_element(By.XPATH,globalConstants.confirmXpath)
        confirm.click()
        
        self.waitForElementVisible((By.XPATH,globalConstants.complateContinueBtnXpath))
        complateContinueBtn = self.driver.find_element(By.XPATH,globalConstants.complateContinueBtnXpath)
        complateContinueBtn.click()

        self.waitForElementVisible((By.XPATH,globalConstants.logoutXpath))
        logout = self.driver.find_element(By.XPATH,globalConstants.logoutXpath)
        logout.click()
    
    
    def waitForElementVisible(self,locator,timeout = 10):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))