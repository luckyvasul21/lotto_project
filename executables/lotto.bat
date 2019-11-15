set workspace=%cd%
set proj_path=%workspace%

behave --no-color --no-capture --no-capture-stderr -f allure_behave.formatter:AllureFormatter -o %proj_path%\result\ %proj_path%\src\lotto.feature