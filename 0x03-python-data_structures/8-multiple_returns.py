#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return ((len(sentense), None))
    else:
        return (len(sentence), sentence[0])
