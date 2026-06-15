@echo off
setlocal

set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

if "%1" == "html" goto html
if "%1" == "clean" goto clean

goto help

:help
echo Please use 'make.bat <target>' where <target> is one of:
echo   html      to build the documentation
echo   clean     to remove built documentation
goto end

:html
%SPHINXBUILD% -b html "%SOURCEDIR%" "%BUILDDIR%\html"
goto end

:clean
if exist "%BUILDDIR%" rmdir /s /q "%BUILDDIR%"
goto end

:end
endlocal
