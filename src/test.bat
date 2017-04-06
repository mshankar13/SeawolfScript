set CLASSPATH="C:\downloads\ANTLR\antlr-4.6-complete.jar;"

java org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener Grammar.g4

python seawolf.py test_01.expr

