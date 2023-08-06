import datetime
from translated.translated import Translated

# To translate greetings into different languages
translated = Translated()


def greeting_by_time(morning=(4, 11), day=(11, 16), evening=(16, 0), night=(0, 4), lang='en') -> str:
    '''greeting_by_time - it's the function to generate a greetings by current time.

    :: morning, day, evening and night - take two* numbers in tuple that are ranges of hours for a certain time of day;
    :: lang - the language** ( lang_code ) in which the greeting will be generated.
    
    * - the first number is the start point of the range, and the second number is the end of the range ( not including it );

    ** - there are 15 languages available, you can view them in the "translated" module.'''


    current_hour = datetime.datetime.now().hour

    if current_hour in range(*morning):
        greeting = 'Good morning'

    elif current_hour in range(*day):
        greeting = 'Good day'

    elif current_hour in range(*evening):
        greeting = 'Good evening'

    elif current_hour in range(*night):
        greeting = 'Good night'

    else:
        greeting = 'Good time of day'


    return translated.translate(text=greeting,
                                from_lang='en',
                                to_lang=lang)







