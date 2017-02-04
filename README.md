# Automizer to Crontab

Frquency depends on the Period.

Frequency becomes seconds, minutes, hours, days depending on what Period was selected.

Period Week, is pretty much the same as Day so translation should be equal.

## To run the Tests
    python -m unittest discover -v

## To use
* Export tasks and schedules from Automizer using delimiter @%%@

    python -m automize_to_crontab_converter [filepath of task] [filepath of schedules]

## To be done
* Implement month period ( i don't need )
* Implement range of crontabs 1,2,3,4 becomes 1-4
* Create a beautiful folder structure

### Reference
    http://www.hiteksoftware.com/help/english/gui/schedulingtasks.htm