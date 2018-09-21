@echo off

:PRE
set PYEXIT=
set HERE=%~dp0

REM push this dir onto dir stack
pushd "%HERE%"

:RUN
echo --- Running main.py
echo.
python main.py
set PYEXIT=%ERRORLEVEL%
echo.
echo --- main.py exited with code %PYEXIT%

:POST
REM pop this dir off dir stack
popd
set PYEXIT=
set HERE=
