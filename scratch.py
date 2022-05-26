import plotly.express as px
import webbrowser


def main():
    add_webbrowser()
    fig = px.bar(y=[2, 1, 3])

    fig.show(renderer='firefox')


def add_webbrowser():
    firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))


if __name__ == '__main__':
    main()
