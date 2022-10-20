# Transaction Project (Algorithm Design)

> Document version: `1.0`\
>Last change on: 11-Oct-2022

- [Transaction Project (Algorithm Design)](#transaction-project-algorithm-design)
  - [Introduction](#introduction)
  - [login page](#login-page)
    - [Customer login](#customer-login)
    - [Admin login](#admin-login)

---

## Introduction

* This documentation is for complete reference to construct the **Transaction software**.

---

## login page

* When user enter the bank website, First he/she will encounter login page.

* There are chances of fraudulent activities(durinig login). Inorder to prevent such kind of activities, The follwing algorithms are used as counter measure.

* Algorithms related to the [user(Customer) login](#customer-login) and [Admin login](#admin-login) are described here.

### Customer login

1. **START**.
2. **GET** *IP_address*. (GOTO:3)
3. **GET** *user_name, upi_password*. (GOTO:4)
4. Check *user_name* existence (GOTO:4.1)

   4.1. **IF** *user_name* exists **THEN** GOTO:5.

   4.2. **ELSE OUTPUT:** *"user doesn't exists!"*. (GOTO:3)

5. Validate *user_name* and *upi_password* and *Account status*. (GOTO:5.1)

   5.1. **IF** *Account status* is *freezed* GOTO: 6.4

   5.2. **IF** *user_name* and *upi_password* matches **THEN** GOTO: 7

   5.3. **ELSE** GOTO:6

6. Since Customer *user_name* and *upi_password* doesn't match GOTO:6.1

    6.1. Create Counter **IF** not exits and yield a count named *login_attempt*. **ELSE** yield *login_attempt*. (GOTO:6.2)

    6.2. **IF** *login_attempt* is greater than 5(constant:MAX_LOGIN_ATTEMPT) **THEN** GOTO:6.3

    6.3. **UPDATE** Customer's accountt status as *freezed* in Database.

    6.4 **OUTPUT** *"Your Account is temporarily freezed, To unfreeze enter the code sent to your email {cutomer email}"*

    6.5. Send account recover email to customer's mail ID with recovery code.

    6.6. **GET** *recovery_code*

    6.7. **IF** *recovery_code* gets matched **THEN UPDATE**  customer's account status as *unfreezed* in Database. (GOTO:3)

    6.8. **ELSE** **OUTPUT** *"Recovery code does not match!"*. (GOTO:6.7)

7. Check for already logged in device information.

    7.1. **IF** no device login found **THEN** **OUTPUT** *"New login found enter the code sent to your mail id."*

    7.2. Send confirm email with verification code.

    7.3. **GET** *verification_code*, **IF** *verification_code* is matched. **UPDATE** The Database with the device information and GOTO:7.4., **ELSE** **OUTPUT** *"verification code doesn't match!"*. (GOTO:7.3)

    7.4 **IF** Device login details found **THEN** GOTO:8

8. Redirect the login page to the account page.

9. STOP

### Admin login

---
