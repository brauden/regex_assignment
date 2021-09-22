# Regular expressions assignment
## Question 1:
**Write a regular expression that matches people's full names.**
```python
pattern = r"[A-Z][a-z\.]+(( [A-Z][-\w,\.]+)+|( [a-z]+ [A-Z][a-z]+)+)"
```

**Describe in what situations your solution will fail.**\

It will fail:
* In a sentence word. Example: Hello. Yes.
* When a person has first name middle name and compound last name.\
Example: Washington Seymur Alan-Michael

## Question 2:
**Develop a regular expression that matches all gerunds within a text.**
```python
pattern = r"(\w+[aeoiu]\w*ing)|(\w+[^aeiouy]y\w*ing)|([^aeoiu\s]y\w*ing)"
```

**Describe in what situations your solution will fail.**\
It will fail:
* With set of words ending with ing but not gerunds. Example: Beijing, evening, morning

## Question 3:
**Generate a regular expression that matches each capturing group in a (Python) regular expression.**
```python
pattern = r"(\(\?[^:=!<].*?\))|(\([^\?].*?\))"
```

**Describe in what situations your solution will fail.**\
It will fail:
* if string contain nested parenthesis and by the assignment condition we are not expecting those.\
Example: ((?<=some text)(\w+))
* with this pattern the regex will fail with empty parenthesis.\
Example: ()(?<!text)
