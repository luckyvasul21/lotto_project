# Created by lpalabatla at 09/02/2018
Feature: Lottery

  Scenario: Get lotto results
    When  user login into application
    And   user on results page
    And   get today draw results
    And   copy the results into lotto sheet