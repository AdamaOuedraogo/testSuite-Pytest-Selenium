
def pytest_addoption(parser):
    parser.addoption("--app-url", action="store", default="http://v2.iris-dev.cabestan.com", help="my option: type1 or type2")
    parser.addoption("--squash-url", action="store", default="https://squash.pupille.cabestan.com/squash-tm/api/rest/latest", help="Squash TM url")
    parser.addoption("--driver", action="store", default="chrome", help="Test Driver eg: chromedriver")
    parser.addoption("--remote", action="store", default=True, help="If remote is provided it will execute on selenim grid")
    parser.addoption("--isAuthenticate", action="store", default="False", help="to know if user is authenticate to the app")
    parser.addoption("--zalenium-hub", action ="store", default="http://localhost:4444/wd/hub", help="hub for watching test on different node")
    parser.addoption("--timeout", action="store", default="20", help="time to wait until element appear")
    parser.addoption("--campaign", action="store", default=None, help="campaign name")

