# Automizer to Crontab

Frquency depends on the Period.

Frequency becomes seconds, minutes, hours, days depending on what Period was selected.

Period Week, is pretty much the same as Day so translation should be equal.

## To run the Tests
    python -m unittest discover -v tests

## To use
* Export tasks and schedules from Automizer using delimiter @%%@

    python -m application.convert (filepath of task) (filepath of schedules)

## To be done
* Implement month period ( i don't need )
* Verify run hours, run days matches rules correctly (specifically on hour period)

### Reference
    http://www.hiteksoftware.com/help/english/gui/schedulingtasks.htm