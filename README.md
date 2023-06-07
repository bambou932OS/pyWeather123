# PyWeather - CLI Weather Application

Did you ever want to know the weather of your city without opening your browser? 

This is the solution for you.

PyWeather is a CLI application that gives you the weather of your city in a matter of seconds.

Even if you are far from the *real-window*, you can know the weather from your closest *terminal-window*.

## Installation

In order to use PyWeather, you need python3.6 or higher installed on your machine.

To install python, go to [python.org](https://www.python.org/downloads/) and download python version 3.6 or higher.

After installing python, Clone this repository to your machine.

```bash
git clone https://github.com/bambou932/pyWeather.git

cd pyWeather
```

After cloning the repository, you can use the application by running the following command:

```bash
python pyWeather.py <city name>
```

For example:

```bash
python pyWeather.py Paris
```

and you will get the following output:

```
The weather in Paris(FR) is 22.58°C.
```

You can also use the application with arguments:

- -h, --help : Show the help message and exit.
- '-c', '-m', '--metric' : Show the temperature in Celsius.
- '-f', '-i', '--imperial' : Show the temperature in Fahrenheit.